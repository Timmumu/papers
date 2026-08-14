# -*- coding: utf-8 -*-
"""Re-match previously-missing included papers against the REBUILT v2 index
(1,740 PDFs, includes user's newly added PDFs). Same medium strictness:
front-matter DOI OR full-title OR author+year filename + title overlap.
Copy + full-extract + verify each candidate.
Output: ss/rematch_round2.txt
"""
import os, re, json, sys, shutil, subprocess
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from screening_data import S
import step3_data

RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
EN_PDF = r'H:\phd\paper\Endnote\My EndNote Library.Data\PDF'
FT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
IDX = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\endnote_index_v2.json'
PWSH = r'h:/phd/6.pjt/LR1/papers/.venv/Scripts/python.exe'
OUT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\rematch_round2.txt'

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
print('Loaded index with', len(idx), 'entries', flush=True)

def norm(s):
    return re.sub(r'[^a-z0-9]', '', s.lower())

def find_path(base):
    return os.path.join(EN_PDF, idx[base]['dir'], base)

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
    cn = norm(c)
    if doi.startswith('10.') and doi in c[:4500]:
        return True, len(c)
    if len(ti_norm) >= 40 and ti_norm in cn[:4000]:
        return True, len(c)
    return False, len(c)

# papers not yet coded (no fulltext so far)
included = [n for n in range(1, 430) if S[n][5] == 'Include']
coded = set(step3_data.S3.keys())
to_check = [n for n in included if n not in coded]
print('papers not yet coded:', len(to_check), flush=True)

lines, found, ambiguous, absent = [], [], [], []
for n in to_check:
    m = meta[n]
    rid, slug, ti_norm, doi = m['rid'], S[n][7], norm(m['ti']), m['doi']
    out_txt = os.path.join(FT, f'{rid}_{slug}.txt')
    out_pdf = os.path.join(FT, f'{rid}_{slug}.pdf')

    doi_hits = [f for f, t in idx.items() if doi.startswith('10.') and doi in t['text']]
    title_hits = []
    if len(ti_norm) >= 30:
        probe = ti_norm[:30]
        title_hits = [f for f, t in idx.items() if probe in norm(t['text'])]
    fname_hits = []
    first = m['first'].lower()
    if first:
        base_probe = first.split()[0]
        for f in idx:
            if f.lower().startswith(base_probe) and m['py'] in f:
                fname_hits.append(f)

    cands, seen = [], set()
    for f in doi_hits + title_hits + fname_hits:
        if f not in seen:
            seen.add(f); cands.append(f)

    if len(cands) == 0:
        absent.append((n, rid, slug)); continue
    # single strong candidate or resolve multiple by full title
    best = None
    if len(cands) == 1:
        best = cands[0]
    else:
        # pick the one whose front matter has the full title or DOI
        strong = []
        for f in cands:
            t = idx[f]['text']
            tn = norm(t)
            if (doi.startswith('10.') and doi in t) or (len(ti_norm) >= 40 and ti_norm in tn):
                strong.append(f)
        if len(strong) == 1:
            best = strong[0]
        else:
            ambiguous.append((n, rid, slug, cands))
            lines.append(f'AMBIG #{n} [{rid}] {slug}: {cands}')
            continue

    src = find_path(best)
    if not os.path.exists(src):
        absent.append((n, rid, slug)); continue
    shutil.copy2(src, out_pdf)
    full_extract(out_pdf, out_txt)
    ok, ln = verify(out_txt, doi, ti_norm)
    if ok and ln >= 4000:
        found.append((n, rid, slug, best, ln))
        lines.append(f'FOUND #{n} [{rid}] {slug} <- {best} len={ln}')
    else:
        # not actually the right paper -> remove copied files
        for p in (out_pdf, out_txt):
            if os.path.exists(p):
                os.remove(p)
        absent.append((n, rid, slug))
        lines.append(f'REJ   #{n} [{rid}] {slug} (candidate {best} failed verify)')

lines.append('')
lines.append(f'FOUND: {len(found)} | AMBIG: {len(ambiguous)} | ABSENT: {len(absent)}')
open(OUT, 'w', encoding='utf-8').write('\n'.join(lines))
print('\n'.join(lines))
print('\nReport:', OUT)
