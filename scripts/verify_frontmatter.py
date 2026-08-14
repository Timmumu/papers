"""Reliable verification: paper's DOI must appear in the FIRST 3500 chars
(front matter / citation block) of its text. This avoids reference-list contamination.
Also requires the filename slug to be a reasonable candidate OR the first-author surname
to appear in the front matter.
"""
import os, re, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from screening_data import S

RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
FT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
OUT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\verify_frontmatter.txt'

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
                   first=aus[0].split(',')[0].strip().lower() if aus else '')

texts = {}
for f in os.listdir(FT):
    if f.endswith('.txt'):
        try:
            texts[f] = open(os.path.join(FT, f), encoding='utf-8', errors='replace').read().lower()
        except Exception:
            pass

def slug_to_idx():
    d = {}
    for n in range(1, 430):
        d[S[n][7]] = n
    return d
S2I = slug_to_idx()

verified, fail = [], []
for n in range(1, 430):
    if S[n][5] != 'Include':
        continue
    m = meta[n]
    doi = m['doi']
    front_ok = False
    matched = None
    for f, c in texts.items():
        front = c[:3500]
        if doi.startswith('10.') and doi in front:
            matched = f
            front_ok = True
            break
    if front_ok:
        verified.append((n, m['rid'], S[n][7], matched))
    else:
        fail.append((n, m['rid'], S[n][7], m['doi'][:40], m['ti'][:55]))

lines = []
lines.append(f'FRONT-MATTER VERIFIED: {len(verified)} | FAIL: {len(fail)}\n')
lines.append('=== VERIFIED ===')
for n, rid, slug, f in verified:
    lines.append(f'#{n} [{rid}] {slug} -> {f}')
lines.append('\n=== FAIL (no front-matter DOI) ===')
for n, rid, slug, doi, ti in fail:
    lines.append(f'#{n} [{rid}] {slug} DOI={doi} | {ti}')

open(OUT, 'w', encoding='utf-8').write('\n'.join(lines))
print(f'front-verified={len(verified)} fail={len(fail)}')
