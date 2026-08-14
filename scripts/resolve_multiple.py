"""Resolve MULTIPLE Endnote candidates + flag tiny/suspicious extracted texts.
For MULTIPLE: pick the candidate whose front-matter title best matches the paper's
title, copy + extract + verify. Flag any verified txt < 4000 bytes as SUSPECT
(real papers extract to tens of KB). Writes ss/resolved_fulltext.txt.
"""
import os, re, json, sys, shutil
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from screening_data import S

RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
EN_PDF = r'H:\phd\paper\Endnote\My EndNote Library.Data\PDF'
FT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
IDX = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\endnote_index.json'
PWSH = r'h:/phd/6.pjt/LR1/papers/.venv/Scripts/python.exe'

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
    meta[n] = dict(rid=field('ID'), ti=field('TI').lower(), doi=field('DO').lower())

idx = json.load(open(IDX, encoding='utf-8'))

def find_path(fname):
    for root, _, fs in os.walk(EN_PDF):
        if fname in fs:
            return os.path.join(root, fname)
    return None

def full_extract(pdf, txt_out):
    code = ('from pypdf import PdfReader; r=PdfReader(r"%s"); '
            'open(r"%s","w",encoding="utf-8").write("\\n".join(p.extract_text() or "" for p in r.pages))'
            % (pdf.replace('"', '\\"'), txt_out.replace('"', '\\"')))
    subprocess = __import__('subprocess')
    subprocess.run([PWSH, '-c', code], capture_output=True, text=True, timeout=180)

def norm(s):
    return re.sub(r'[^a-z0-9]', '', s)

MULTIPLE = {
    265: '10.1007/s13349-023-00751-z',
    376: '10.1108/ecam-05-2025-0732',
    423: None,  # find DOI from meta
}
for n, doi in list(MULTIPLE.items()):
    if doi is None:
        doi = meta[n]['doi']
    hits = [f for f, t in idx.items() if doi in t]
    print(f'#{n} [{meta[n]["rid"]}] {S[n][7]} DOI={doi}')
    print('  candidates:', hits)
    # pick best by title overlap with front matter
    target = norm(meta[n]['ti'])
    best, bestscore = None, -1
    for f in hits:
        t = norm(idx[f])
        # score = number of consecutive title chars present
        score = 0
        for i in range(10, len(target), 10):
            if target[:i] in t:
                score = i
        print(f'    {f}: score={score}')
        if score > bestscore:
            best, bestscore = f, score
    if best:
        src = find_path(best)
        slug = S[n][7]
        out_pdf = os.path.join(FT, f'{meta[n]["rid"]}_{slug}.pdf')
        out_txt = os.path.join(FT, f'{meta[n]["rid"]}_{slug}.txt')
        shutil.copy2(src, out_pdf)
        full_extract(out_pdf, out_txt)
        c = open(out_txt, encoding='utf-8', errors='replace').read()
        ok = doi in c[:4500]
        print(f'  -> copied {best}; verified={ok}; len={len(c)}')
    else:
        print('  !! no candidate')

# flag suspicious verified files (too small)
print('\n=== SUSPECT (verified but < 4000 bytes or no pdf) ===')
for f in sorted(os.listdir(FT)):
    if f.endswith('.txt'):
        p = os.path.join(FT, f)
        sz = os.path.getsize(p)
        if sz < 4000:
            print(f'  {f}: {sz} bytes')
