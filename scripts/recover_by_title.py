"""Second recovery pass: for missing included papers, search Endnote index front
matter for a distinctive title substring (>=35 normalized chars). Single hit with
good score -> copy + extract + verify DOI/title. Writes ss/title_recovery.txt.
"""
import os, re, json, sys, shutil, subprocess
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from screening_data import S

RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
EN_PDF = r'H:\phd\paper\Endnote\My EndNote Library.Data\PDF'
FT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
IDX = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\endnote_index.json'
PWSH = r'h:/phd/6.pjt/LR1/papers/.venv/Scripts/python.exe'
OUT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\title_recovery.txt'

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

def norm(s):
    return re.sub(r'[^a-z0-9]', '', s)

def find_path(fname):
    for root, _, fs in os.walk(EN_PDF):
        if fname in fs:
            return os.path.join(root, fname)
    return None

def full_extract(pdf, txt_out):
    code = (f'from pypdf import PdfReader; r=PdfReader(r"{pdf}"); '
            f'open(r"{txt_out}","w",encoding="utf-8").write("\\n".join(p.extract_text() or "" for p in r.pages))')
    subprocess.run([PWSH, '-c', code], capture_output=True, text=True, timeout=180)

# which included papers already have verified fulltext files?
already = set()
for f in os.listdir(FT):
    if f.endswith('.txt'):
        already.add(f.split('_')[0])

lines = []
recovered, still_missing = [], []
included = [n for n in range(1, 430) if S[n][5] == 'Include']
for n in included:
    rid = meta[n]['rid']
    if rid in already:
        continue
    doi = meta[n]['doi']
    ti_norm = norm(meta[n]['ti'])
    if len(ti_norm) < 35:
        continue
    # distinctive substrings of the title
    probes = []
    L = len(ti_norm)
    probes.append(ti_norm[:int(L*0.6)])
    probes.append(ti_norm[L//5:L//5+int(L*0.5)])
    # find candidate Endnote files whose front matter contains probe
    hits = set()
    for probe in probes:
        if len(probe) < 25:
            continue
        for f, t in idx.items():
            if probe in t:
                hits.add(f)
    if len(hits) == 1:
        fname = list(hits)[0]
        # verify title strongly present
        if ti_norm[:35] in norm(idx[fname]) or len(ti_norm) >= 50 and ti_norm[10:60] in norm(idx[fname]):
            src = find_path(fname)
            if src:
                out_pdf = os.path.join(FT, f'{rid}_{S[n][7]}.pdf')
                out_txt = os.path.join(FT, f'{rid}_{S[n][7]}.txt')
                shutil.copy2(src, out_pdf)
                full_extract(out_pdf, out_txt)
                c = open(out_txt, encoding='utf-8', errors='replace').read().lower()
                ok = (doi.startswith('10.') and doi in c[:4500]) or (ti_norm[:35] in norm(c[:4000]))
                if ok and len(c) > 4000:
                    recovered.append((n, rid, S[n][7], fname, len(c)))
                    lines.append(f'RECOVERED #{n} [{rid}] {S[n][7]} <- {fname} (len={len(c)})')
                else:
                    still_missing.append((n, rid, S[n][7], 'extract-failed', ''))
    elif len(hits) > 1:
        still_missing.append((n, rid, S[n][7], 'MULTI-title', ','.join(list(hits)[:3])))
    else:
        still_missing.append((n, rid, S[n][7], 'no-title-hit', ''))

open(OUT, 'w', encoding='utf-8').write('\n'.join(lines + [f'\nrecovered={len(recovered)}']))
print('\n'.join(lines))
print(f'\nrecovered={len(recovered)} still_missing={len(still_missing)}')
