# -*- coding: utf-8 -*-
"""Generate a reference list of included papers whose PDF was NOT found in the
Endnote library (coverage re-scan 2026-08-12), enriched with title/journal/DOI,
so the user can hunt for the PDFs and add them to Endnote.

Output: 04c_LR 3round/ss/missing_endnote_pdfs.md
"""
import os, re, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from screening_data import S
import step3_data

FT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
OUT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\missing_endnote_pdfs.md'

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
    meta[n] = dict(rid=field('ID'), ti=field('TI'), doi=field('DO'),
                   jr=field('J2') or field('JF') or field('JO'),
                   py=field('PY'), au=(aus[0].split(',')[0].strip() if aus else ''))

def norm(s):
    return re.sub(r'[^a-z0-9]', '', s.lower())

# rids that have a verified fulltext on disk (Endnote or OA)
verified = set()
for f in os.listdir(FT):
    if f.endswith('.txt') and os.path.getsize(os.path.join(FT, f)) >= 4000:
        verified.add(f.split('_')[0])

# coded indices
coded = set(step3_data.S3.keys())

rows = []
included = [n for n in range(1, 430) if S[n][5] == 'Include']
for n in included:
    m = meta[n]
    # has verified fulltext on disk?
    fn = [f for f in os.listdir(FT) if f.startswith(m['rid'] + '_') and f.endswith('.txt')]
    ok = False
    if fn:
        c = open(os.path.join(FT, fn[0]), encoding='utf-8', errors='replace').read().lower()
        cn = norm(c)
        tn = norm(m['ti'])
        if m['doi'].startswith('10.') and m['doi'].lower() in c[:4500]:
            ok = True
        elif len(tn) >= 40 and tn in cn[:4000]:
            ok = True
    if ok:
        continue  # fulltext available (Endnote or OA)
    # not available -> flag whether coded anyway (via OA) or not yet coded
    already_coded = n in coded
    rows.append((n, m['rid'], S[n][7], m['au'], m['py'], m['ti'], m['jr'], m['doi'], already_coded))

rows.sort(key=lambda x: (x[8], x[0]))  # coded-first then index

lines = []
lines.append('# Included papers with NO PDF found in Endnote (reference list)')
lines.append('')
lines.append('Coverage re-scan date: 2026-08-12. Use this to locate PDFs and add them to Endnote.')
lines.append('')
lines.append(f'Total: **{len(rows)}** included papers without a verified Endnote PDF.')
lines.append('')
nc = sum(1 for r in rows if not r[8])
lines.append(f'- **{nc} not yet coded** (no fulltext anywhere) — prioritise these')
lines.append(f'- **{len(rows) - nc} already coded** via open-access/other source (PDF still not in Endnote)')
lines.append('')
lines.append('| # | ID | Citekey | Author | Year | Title | Journal | DOI |')
lines.append('|---|-----|---------|--------|------|-------|---------|-----|')
for n, rid, slug, au, py, ti, jr, doi, ac in rows:
    tag = ' [CODED-via-OA]' if ac else ''
    lines.append(f'| {n} | {rid} | `{slug}` | {au} | {py} | {ti} | {jr} | {doi} |{tag}')

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f'Wrote {OUT} with {len(rows)} rows')
print(f'  not-yet-coded: {nc} | already-coded-via-OA: {len(rows) - nc}')
