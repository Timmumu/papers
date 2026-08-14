"""Scan ALL Endnote-attached PDFs: for each included paper (by DOI), find Endnote
PDFs whose FRONT MATTER (first 2 pages) contains that DOI. This reliably identifies
the correct full text regardless of filename. Then copy + full-extract + verify.
"""
import os, re, sys, subprocess
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from screening_data import S

RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
EN_PDF = r'H:\phd\paper\Endnote\My EndNote Library.Data\PDF'
FT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
PWSH = r'h:/phd/6.pjt/LR1/papers/.venv/Scripts/python.exe'
INDEX = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\endnote_index.json'
os.makedirs(FT, exist_ok=True)

# 1. build/load front-matter index of all Endnote PDFs
def build_index():
    import json
    from pypdf import PdfReader
    idx = {}
    files = []
    for root, _, fs in os.walk(EN_PDF):
        for f in fs:
            if f.lower().endswith('.pdf'):
                files.append(os.path.join(root, f))
    print('indexing', len(files), 'endnote pdfs...', flush=True)
    for i, p in enumerate(files):
        t = ''
        try:
            r = PdfReader(p)
            t = ' '.join((pg.extract_text() or '') for pg in r.pages[:2]).lower()
            t = re.sub(r'\s+', ' ', t)[:2000]
        except Exception:
            t = ''
        idx[os.path.basename(p)] = t
        if (i + 1) % 400 == 0:
            print(f'  ...{i+1}', flush=True)
            json.dump(idx, open(INDEX, 'w', encoding='utf-8'))
    json.dump(idx, open(INDEX, 'w', encoding='utf-8'))
    return idx

import json
if os.path.exists(INDEX):
    idx = json.load(open(INDEX, encoding='utf-8'))
    print('loaded index with', len(idx), 'entries')
else:
    idx = build_index()

# 2. parse RIS metadata
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
    meta[n] = dict(rid=field('ID'), ti=field('TI'), doi=field('DO').lower())

def full_extract(pdf, txt_out):
    code = ('from pypdf import PdfReader; r=PdfReader(r"%s"); '
            'open(r"%s","w",encoding="utf-8").write("\\n".join(p.extract_text() or "" for p in r.pages))'
            % (pdf.replace('"', '\\"'), txt_out.replace('"', '\\"')))
    subprocess.run([PWSH, '-c', code], capture_output=True, text=True, timeout=180)
    return os.path.exists(txt_out)

def verify(txt_path, doi):
    try:
        c = open(txt_path, encoding='utf-8', errors='replace').read().lower()
    except Exception:
        return False
    return doi.startswith('10.') and doi in c[:4500]

included = [n for n in range(1, 430) if S[n][5] == 'Include']
found, missing = [], []
for n in included:
    m = meta[n]
    slug = S[n][7]
    out_txt = os.path.join(FT, f'{m["rid"]}_{slug}.txt')
    if os.path.exists(out_txt) and verify(out_txt, m['doi']):
        found.append((n, 'have', ''))
        continue
    doi = m['doi']
    if not doi.startswith('10.'):
        missing.append((n, m['rid'], slug, '(no DOI)'))
        continue
    hits = [f for f, t in idx.items() if doi in t]
    if len(hits) == 1:
        src = os.path.join(EN_PDF, [d for _, d, fs in os.walk(EN_PDF) for f in fs if f == hits[0]][0]) if False else None
        # locate full path
        src = None
        for root, _, fs in os.walk(EN_PDF):
            if hits[0] in fs:
                src = os.path.join(root, hits[0])
                break
        if src:
            import shutil
            out_pdf = os.path.join(FT, f'{m["rid"]}_{slug}.pdf')
            shutil.copy2(src, out_pdf)
            if full_extract(out_pdf, out_txt) and verify(out_txt, doi):
                found.append((n, 'endnote-verified', hits[0]))
            else:
                found.append((n, 'ENDNOTE-UNVERIFIED', hits[0]))
        else:
            missing.append((n, m['rid'], slug, doi))
    elif len(hits) > 1:
        found.append((n, 'MULTIPLE', ','.join(hits[:3])))
    else:
        missing.append((n, m['rid'], slug, doi))

ok = sum(1 for v in found if v[1] in ('have', 'endnote-verified'))
print(f'\nFOUND/verified: {ok} | total handled: {len(found)} | missing: {len(missing)}')
print('\n=== DETAIL ===')
for v in found:
    if v[1] not in ('have',):
        print(f'#{v[0]} [{meta[v[0]]["rid"]}] {S[v[0]][7]} -> {v[1]} {v[2]}')
print('\n=== MISSING (no Endnote front-matter DOI) ===')
for n, rid, slug, doi in missing:
    print(f'#{n} [{rid}] {slug} DOI={doi or "-"} | {meta[n]["ti"][:55]}')
