"""Re-match ALL 165 included papers against the REBUILT Endnote index (v2).

Uses MEDIUM strictness (user-approved):
  1. PRIMARY  : paper's DOI present in the PDF's front-matter text (4 pages, 8000 chars).
  2. SECONDARY: paper's normalized title present in the PDF's front-matter text.
  3. TERTIARY : Endnote filename starts with first-author surname + contains year,
                AND paper's normalized title overlaps the PDF's front-matter text.

For every candidate found: copy PDF -> full-extract -> verify identity
(DOI in first 4500 chars OR normalized title present in first 4000 chars),
same strictness as verify_fulltext_final.py.

Output: 04c_LR 3round/ss/coverage_report.txt  (the user-requested deliverable)
Also writes: 04c_LR 3round/ss/coverage_match.json (machine-readable)
"""
import os, re, json, sys, shutil, subprocess, time

sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from screening_data import S

RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
EN_PDF = r'H:\phd\paper\Endnote\My EndNote Library.Data\PDF'
FT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
IDX = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\endnote_index_v2.json'
PWSH = r'h:/phd/6.pjt/LR1/papers/.venv/Scripts/python.exe'
OUT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\coverage_report.txt'
OUTJSON = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\coverage_match.json'

# ---- parse RIS metadata ----
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

# ---- load v2 index ----
idx = json.load(open(IDX, encoding='utf-8'))
print(f'Loaded v2 index with {len(idx)} entries', flush=True)

def norm(s):
    return re.sub(r'[^a-z0-9]', '', s.lower())

# build reverse lookup basename -> full path using stored 'dir'
def find_path(base):
    d = idx[base]['dir']
    return os.path.join(EN_PDF, d, base)

def full_extract(pdf, txt_out):
    code = ('from pypdf import PdfReader; r=PdfReader(r"%s"); '
            'open(r"%s","w",encoding="utf-8").write("\\n".join(p.extract_text() or "" for p in r.pages))'
            % (pdf.replace('"', '\\"'), txt_out.replace('"', '\\"')))
    subprocess.run([PWSH, '-c', code], capture_output=True, text=True, timeout=180)

def verify(txt_path, doi, ti_norm):
    try:
        c = open(txt_path, encoding='utf-8', errors='replace').read().lower()
    except Exception:
        return False, 0
    ok = False
    reason = ''
    if doi.startswith('10.') and doi in c[:4500]:
        ok, reason = True, 'doi'
    elif ti_norm and len(ti_norm) >= 30 and ti_norm[:30] in norm(c[:4000]):
        ok, reason = True, 'title'
    return ok, reason, len(c)

included = [n for n in range(1, 430) if S[n][5] == 'Include']
results = {}
counts = {'already_have': 0, 'found_verified': 0, 'candidate_found': 0,
          'candidate_unverified': 0, 'ambiguous': 0, 'absent': 0}

lines = []
lines.append('=== ENDNOTE COVERAGE RE-MATCH (medium strictness) ===')
lines.append('')
lines.append(f'INDEX: {len(idx)} PDFs | INCLUDED: {len(included)}')

for n in included:
    m = meta[n]
    rid = m['rid']
    slug = S[n][7]
    ti_norm = norm(m['ti'])
    doi = m['doi']
    out_txt = os.path.join(FT, f'{rid}_{slug}.txt')
    out_pdf = os.path.join(FT, f'{rid}_{slug}.pdf')

    # 0) already verified full text on disk
    if os.path.exists(out_txt) and os.path.exists(out_pdf):
        ok, reason, ln = verify(out_txt, doi, ti_norm)
        if ok and ln >= 4000:
            results[rid] = dict(status='already_have', file=f'{rid}_{slug}.txt',
                                method='existing', reason=reason, n=n)
            counts['already_have'] += 1
            continue

    # 1) DOI hit in front matter
    doi_hits = [f for f, t in idx.items() if doi.startswith('10.') and doi in t['text']]

    # 2) title hit in front matter
    title_hits = []
    if len(ti_norm) >= 30:
        probe = ti_norm[:30]
        title_hits = [f for f, t in idx.items() if probe in norm(t['text'])]

    # 3) filename author+year candidates
    fname_hits = []
    first = m['first'].lower()
    if first:
        base_probe = first.split()[0] if ' ' in first else first
        for f, t in idx.items():
            low = f.lower()
            if low.startswith(base_probe) and m['py'] in f:
                fname_hits.append(f)

    # union, dedupe, keep order of confidence
    candidates = []
    seen = set()
    for f in doi_hits + title_hits + fname_hits:
        if f not in seen:
            seen.add(f)
            candidates.append(f)

    if len(candidates) == 0:
        results[rid] = dict(status='absent', n=n)
        counts['absent'] += 1
        lines.append(f'ABSENT  #{n} [{rid}] {slug}')
        continue

    if len(candidates) > 1:
        results[rid] = dict(status='ambiguous', files=candidates, n=n)
        counts['ambiguous'] += 1
        lines.append(f'AMBIG   #{n} [{rid}] {slug}  files={candidates}')
        continue

    # single candidate: copy + extract + verify
    f = candidates[0]
    src = find_path(f)
    if not src or not os.path.exists(src):
        results[rid] = dict(status='absent', n=n, why='path-missing')
        counts['absent'] += 1
        lines.append(f'ABSENT  #{n} [{rid}] {slug} (path missing)')
        continue
    shutil.copy2(src, out_pdf)
    full_extract(out_pdf, out_txt)
    ok, reason, ln = verify(out_txt, doi, ti_norm)
    if ok and ln >= 4000:
        method = 'doi' if f in doi_hits else ('title' if f in title_hits else 'fname+title')
        results[rid] = dict(status='found_verified', file=f'{rid}_{slug}.txt',
                            method=method, reason=reason, endnote_file=f, n=n, len=ln)
        counts['found_verified'] += 1
        lines.append(f'FOUND   #{n} [{rid}] {slug}  <- {f}  [{method}/{reason}] len={ln}')
    else:
        results[rid] = dict(status='candidate_unverified', file=f'{rid}_{slug}.txt',
                            endnote_file=f, n=n, len=ln, reason=reason)
        counts['candidate_unverified'] += 1
        lines.append(f'UNVER   #{n} [{rid}] {slug}  <- {f}  (len={ln} reason={reason})')

lines.append('')
lines.append('=== SUMMARY ===')
for k, v in counts.items():
    lines.append(f'{k}: {v}')
lines.append(f'FOUND-ON-ENDNOTE: {counts["already_have"] + counts["found_verified"]} / {len(included)}')

open(OUT, 'w', encoding='utf-8').write('\n'.join(lines))
json.dump(results, open(OUTJSON, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('\n'.join(lines))
print(f'\nReport: {OUT}')
