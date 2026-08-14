"""DEFINITIVE mapping: for each included paper, the .txt file whose content contains
that paper's FULL DOI (strict). No short-substring fallback. Output:
  - verified: paper -> correct text file
  - unverified: paper has no DOI-confirmed text (needs re-fetch or Endnote manual check)
"""
import os, re, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from screening_data import S

RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
FT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
OUT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\definitive_map.txt'

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
    do = field('DO').lower().strip()
    meta[n] = dict(rid=field('ID'), ti=field('TI'), doi=do)

def doi_forms(doi):
    """Strict full-DOI variants that appear inside PDF text (which may line-wrap)."""
    if not doi or not doi.startswith('10.'):
        return []
    core = doi[3:]  # after '10.'
    return [
        doi,                                   # 10.1000/abc
        doi.replace('/', '%2F'),               # url-encoded
        'doi.org/' + doi,                      # with domain
    ]

texts = {}
for f in os.listdir(FT):
    if f.endswith('.txt'):
        try:
            texts[f] = open(os.path.join(FT, f), encoding='utf-8', errors='replace').read().lower()
        except Exception:
            pass

verified, unverified, ambiguous = [], [], []
for n in range(1, 430):
    if S[n][5] != 'Include':
        continue
    doi = meta[n]['doi']
    forms = doi_forms(doi)
    hits = []
    for f, c in texts.items():
        for form in forms:
            if form in c:
                hits.append(f)
                break
    hits = sorted(set(hits))
    if len(hits) == 1:
        verified.append((n, meta[n]['rid'], S[n][7], hits[0]))
    elif len(hits) > 1:
        ambiguous.append((n, meta[n]['rid'], S[n][7], hits, doi))
    else:
        unverified.append((n, meta[n]['rid'], S[n][7], doi, meta[n]['ti'][:60]))

lines = []
lines.append(f'VERIFIED: {len(verified)} | UNVERIFIED: {len(unverified)} | AMBIGUOUS: {len(ambiguous)}\n')
lines.append('=== VERIFIED (DOI-confirmed) ===')
for n, rid, slug, f in verified:
    lines.append(f'#{n} [{rid}] {slug} -> {f}')
lines.append('\n=== AMBIGUOUS (DOI in >1 file) ===')
for n, rid, slug, hits, doi in ambiguous:
    lines.append(f'#{n} [{rid}] {slug} DOI={doi} files={hits}')
lines.append('\n=== UNVERIFIED (no DOI-confirmed text) ===')
for n, rid, slug, doi, ti in unverified:
    lines.append(f'#{n} [{rid}] {slug} DOI={doi or "-"} | {ti}')

open(OUT, 'w', encoding='utf-8').write('\n'.join(lines))
print(f'verified={len(verified)} unverified={len(unverified)} ambiguous={len(ambiguous)}')
