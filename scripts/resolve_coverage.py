"""Rigorous resolution of ambiguous + candidate_unverified results from the
coverage re-match.

Problem: the first pass used a 30-char title probe + filename author+year, which
produced false candidates (e.g. a paper matched the WRONG author's file). We must
not count those.

This pass, for every paper with status in {ambiguous, candidate_unverified}:
  1. Load the candidate file(s) front-matter from the v2 index.
  2. Score each candidate:
       - +3 if the paper's exact DOI is in the candidate's front matter.
       - +2 if the paper's FULL normalized title (>=40 chars) is a contiguous
         substring of the candidate's front matter.
       - +1 if a distinctive 40-char title probe is present.
       - +1 if the Endnote filename starts with the paper's first-author surname
         AND the title probe is present (medium strictness).
  3. If exactly ONE candidate scores >= 2 AND (doi OR full-title), copy + extract
     + verify (DOI in first 4500 OR full-title in first 4000). -> FOUND.
  4. If no candidate is reliable -> ABSENT (or uncertain, reported separately).

Output: ss/coverage_final_report.txt + ss/coverage_final.json
"""
import os, re, json, sys, shutil, subprocess

sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from screening_data import S

RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
EN_PDF = r'H:\phd\paper\Endnote\My EndNote Library.Data\PDF'
FT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
IDX = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\endnote_index_v2.json'
PWSH = r'h:/phd/6.pjt/LR1/papers/.venv/Scripts/python.exe'
MATCH = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\coverage_match.json'
OUT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\coverage_final_report.txt'
OUTJSON = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\coverage_final.json'

# ---- parse RIS ----
txt = open(RIS, encoding='utf-8', errors='replace').read()
recs = re.split(r'\nER  -\s*\n', txt)
meta = {}
n = 0
for r in recs:
    if 'TY  -' not in r:
        continue
    n += 1
    def field(tag):
        m = re.search(rf'^{tag}  - (.*?)(?=^[A-Z0-9]{{2}}  - |\Z)', r, re.M | re.S)
        return ' '.join(m.group(1).split()) if m else ''
    aus = re.findall(r'^AU  - (.*)$', r, re.M)
    meta[n] = dict(rid=field('ID'), ti=field('TI'), doi=field('DO').lower(),
                   first=(aus[0].split(',')[0].strip() if aus else ''), py=field('PY'))

idx = json.load(open(IDX, encoding='utf-8'))
match = json.load(open(MATCH, encoding='utf-8'))

def norm(s):
    return re.sub(r'[^a-z0-9]', '', s.lower())

def find_path(base):
    d = idx[base]['dir']
    return os.path.join(EN_PDF, d, base)

def full_extract(pdf, txt_out):
    code = ('from pypdf import PdfReader; r=PdfReader(r"%s"); '
            'open(r"%s","w",encoding="utf-8").write("\\n".join(p.extract_text() or "" for p in r.pages))'
            % (pdf.replace('"', '\\"'), txt_out.replace('"', '\\"')))
    subprocess.run([PWSH, '-c', code], capture_output=True, text=True, timeout=180)

def verify(txt_path, doi, ti_full):
    try:
        c = open(txt_path, encoding='utf-8', errors='replace').read().lower()
    except Exception:
        return False, '', 0
    cn = norm(c)
    if doi.startswith('10.') and doi in c[:4500]:
        return True, 'doi', len(c)
    if ti_full and len(ti_full) >= 40 and ti_full in cn[:4000]:
        return True, 'title', len(c)
    return False, '', len(c)

def score_candidate(f, paper):
    """Score a candidate Endnote file against a paper. Returns (score, signals)."""
    m = idx.get(f)
    if not m:
        return -99, []
    t = m['text']
    tn = norm(t)
    doi = paper['doi']
    ti_full = norm(paper['ti'])
    signals = []
    score = 0
    if doi.startswith('10.') and doi in t:
        score += 3; signals.append('doi')
    if len(ti_full) >= 40 and ti_full in tn:
        score += 2; signals.append('fulltitle')
    # distinctive 40-char probe from middle of title
    probe = ti_full[10:50] if len(ti_full) >= 50 else ti_full
    if len(probe) >= 30 and probe in tn:
        score += 1; signals.append('probe')
    # filename author+year
    first = paper['first'].lower()
    if first:
        base = first.split()[0]
        if f.lower().startswith(base) and paper['py'] in f:
            score += 1; signals.append('fname')
    return score, signals

def has_strong_signal(signals):
    return 'doi' in signals or 'fulltitle' in signals

def resolve(rid, n, slug, candidates):
    """Try to find exactly one reliable candidate. Returns (status, file, method, len)."""
    paper = meta[n]
    scored = []
    for f in candidates:
        s, sig = score_candidate(f, paper)
        scored.append((s, sig, f))
    scored.sort(reverse=True)
    top_score, top_sig, top_f = scored[0]
    # accept if single candidate with strong signal, or clear winner
    strong = [x for x in scored if x[0] >= 2 and has_strong_signal(x[1])]
    if len(strong) == 1:
        s, sig, f = strong[0]
        if os.path.exists(find_path(f)):
            out_pdf = os.path.join(FT, f'{rid}_{slug}.pdf')
            out_txt = os.path.join(FT, f'{rid}_{slug}.txt')
            shutil.copy2(find_path(f), out_pdf)
            full_extract(out_pdf, out_txt)
            ok, reason, ln = verify(out_txt, paper['doi'], norm(paper['ti']))
            if ok and ln >= 4000:
                return ('found_verified', f, '/'.join(sig), ln)
            else:
                return ('unverified', f, '/'.join(sig), ln)
    # also handle: single candidate overall that has a strong signal
    if top_score >= 2 and has_strong_signal(top_sig) and len(scored) == 1:
        f = top_f
        if os.path.exists(find_path(f)):
            out_pdf = os.path.join(FT, f'{rid}_{slug}.pdf')
            out_txt = os.path.join(FT, f'{rid}_{slug}.txt')
            shutil.copy2(find_path(f), out_pdf)
            full_extract(out_pdf, out_txt)
            ok, reason, ln = verify(out_txt, paper['doi'], norm(paper['ti']))
            if ok and ln >= 4000:
                return ('found_verified', f, '/'.join(top_sig), ln)
            else:
                return ('unverified', f, '/'.join(top_sig), ln)
    return (None, None, None, 0)

# gather papers to resolve
to_resolve = {}
for rid, v in match.items():
    if v['status'] in ('ambiguous', 'candidate_unverified'):
        n = v['n']
        if v['status'] == 'ambiguous':
            cands = v['files']
        else:
            cands = [v['endnote_file']]
        to_resolve[rid] = (n, cands)

results = {}
found_new, still_unresolved = [], []
for rid, (n, cands) in to_resolve.items():
    slug = S[n][7]
    st, f, method, ln = resolve(rid, n, slug, cands)
    if st == 'found_verified':
        results[rid] = dict(status='found_verified', file=f'{rid}_{slug}.txt',
                            endnote_file=f, method=method, n=n, len=ln)
        found_new.append((n, rid, slug, f, method, ln))
    elif st == 'unverified':
        results[rid] = dict(status='unverified', endnote_file=f, method=method, n=n, len=ln)
        still_unresolved.append((n, rid, slug, f, 'unverified'))
    else:
        results[rid] = dict(status='absent', n=n)
        still_unresolved.append((n, rid, slug, '?', 'absent'))

lines = []
lines.append('=== COVERAGE FINAL RESOLUTION (strict) ===')
lines.append('')
lines.append(f'RESOLVED-NEW-FOUND: {len(found_new)}')
for n, rid, slug, f, method, ln in sorted(found_new):
    lines.append(f'FOUND  #{n} [{rid}] {slug}  <- {f}  [{method}] len={ln}')
lines.append('')
lines.append(f'STILL UNRESOLVED: {len(still_unresolved)}')
for n, rid, slug, f, why in sorted(still_unresolved):
    lines.append(f'{why.upper()}  #{n} [{rid}] {slug}  <- {f}')

open(OUT, 'w', encoding='utf-8').write('\n'.join(lines))
json.dump(results, open(OUTJSON, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('\n'.join(lines))
print(f'\nReport: {OUT}')
