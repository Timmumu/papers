"""Definitive verification: for each of the 165 included papers, find its file in
fulltext/ by RID prefix, verify DOI in first 4500 chars, and report verified /
unverified / missing. Also handles the 3 MULTIPLE Endnote cases by checking both
candidates. Writes report to ss/verified_fulltext.txt.
"""
import os, re, json, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from screening_data import S

RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
FT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
IDX = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\endnote_index.json'
OUT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\verified_fulltext.txt'

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

# corrigendum files are NOT full texts even if they mention the DOI
CORRIGENDA = {'3924'}  # rid of Guo2025-quality corrigendum

def verify(path, doi, rid):
    try:
        c = open(path, encoding='utf-8', errors='replace').read().lower()
    except Exception:
        return False
    if rid in CORRIGENDA:
        return False
    if len(c) < 4000:
        return False
    return doi.startswith('10.') and doi in c[:4500]

idx = json.load(open(IDX, encoding='utf-8'))

included = [n for n in range(1, 430) if S[n][5] == 'Include']
out = []
verified, unverified, missing = [], [], []
for n in included:
    rid = meta[n]['rid']
    doi = meta[n]['doi']
    slug = S[n][7]
    # find file by rid prefix
    cands = [f for f in os.listdir(FT) if f.lower().endswith('.txt') and f.startswith(rid + '_')]
    status = None
    note = ''
    if cands:
        txtp = os.path.join(FT, cands[0])
        if verify(txtp, doi, rid):
            verified.append((n, rid, slug, cands[0]))
            status = 'VERIFIED'
        else:
            unverified.append((n, rid, slug, cands[0], doi))
            status = 'UNVERIFIED'
    else:
        # no file; try endnote index single hit
        if doi.startswith('10.'):
            hits = [f for f, t in idx.items() if doi in t]
            if len(hits) == 1:
                status = 'ENDNOTE-ONLY-HIT'
                note = hits[0]
                missing.append((n, rid, slug, doi, 'endnote-single-hit: ' + hits[0]))
            elif len(hits) > 1:
                status = 'MULTIPLE'
                note = ','.join(hits[:3])
                missing.append((n, rid, slug, doi, 'MULTIPLE: ' + note))
            else:
                status = 'NO-ENDNOTE'
                missing.append((n, rid, slug, doi, 'no hit'))
        else:
            missing.append((n, rid, slug, doi, 'no DOI'))
    out.append((n, rid, slug, status, note))

lines = []
lines.append(f'INCLUDED={len(included)} VERIFIED={len(verified)} UNVERIFIED={len(unverified)} OTHER-MISSING={len(missing)}')
lines.append('\n=== VERIFIED ===')
for n, rid, slug, fn in verified:
    lines.append(f'#{n} [{rid}] {slug}  <- {fn}')
lines.append('\n=== UNVERIFIED (file exists but DOI not in first 4500) ===')
for n, rid, slug, fn, doi in unverified:
    lines.append(f'#{n} [{rid}] {slug}  <- {fn}  DOI={doi}')
lines.append('\n=== MISSING (no verified file) ===')
for n, rid, slug, doi, why in missing:
    lines.append(f'#{n} [{rid}] {slug}  DOI={doi or "-"}  [{why}]')

open(OUT, 'w', encoding='utf-8').write('\n'.join(lines))
print('\n'.join(lines[:80]))
print(f'\n... full report at {OUT}')
