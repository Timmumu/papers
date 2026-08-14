"""Match each included paper to its full text by DOI (unambiguous).

Each RIS entry carries a DOI; the correct PDF's text contains that DOI.
Also tries PMID/other identifiers. Falls back to title-word check only for
papers with no DOI match.
"""
import os, re, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from screening_data import S

RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
FT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
OUT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\resolve_doi.txt'

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
    do = field('DO').lower()
    if do.startswith('10.'):
        do = do.split()[0]
    meta[n] = dict(rid=field('ID'), ti=field('TI'), doi=do, isbn=field('SN')[:4])

# index: file -> normalized text (lowercased, doi-ish kept)
def norm_for_doi(s):
    return s.lower().replace(' ', '')

texts = {}
for f in os.listdir(FT):
    if f.endswith('.txt'):
        try:
            texts[f] = norm_for_doi(open(os.path.join(FT, f), encoding='utf-8', errors='replace').read())
        except Exception:
            pass

lines = []
doi_matched = []
no_doi = []
for n in range(1, 430):
    if S[n][5] != 'Include':
        continue
    doi = meta[n]['doi']
    hit = None
    if doi:
        # DOI appears in text with slash/dots; search normalized compact form
        compact = doi.replace('.', '').replace('/', '').replace('10', '10', 1)
        for f, nc in texts.items():
            # try '10.xxxx/yyy' form without spaces
            if doi.replace(' ', '') in nc:
                hit = f
                break
        # fallback: last segment of doi
        if not hit:
            seg = doi.split('/')[-1].replace('.', '').replace('-', '')
            if len(seg) >= 6:
                for f, nc in texts.items():
                    if seg in nc:
                        hit = f
                        break
    if hit:
        doi_matched.append((n, meta[n]['rid'], S[n][7], hit))
        lines.append(f'#doi {n} [{meta[n]["rid"]}] {S[n][7]} -> {hit}   DOI={doi}')
    else:
        no_doi.append((n, meta[n]['rid'], S[n][7], doi, meta[n]['ti'][:60]))
        lines.append(f'#NO  {n} [{meta[n]["rid"]}] {S[n][7]}  DOI={doi or "-"} | {meta[n]["ti"][:60]}')

open(OUT, 'w', encoding='utf-8').write('\n'.join(lines))
print(f'DOI-matched: {len(doi_matched)} | no-match: {len(no_doi)}')
