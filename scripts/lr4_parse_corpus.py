# -*- coding: utf-8 -*-
"""LR4 Phase 1: parse the 956-record merged corpus CSV into a compact JSON
store plus small screening worksheet chunks for batch reading.

Outputs (all under 04d_LR4/5. SLR matrix/ss/):
  - corpus_lr4.json      : authoritative LR4 metadata store (row-keyed)
  - screen/chunkNN.txt   : compact title/abstract/keyword worksheets
"""
import csv, json, os, re, unicodedata

ROOT = r'h:\phd\6.pjt\LR1\papers'
CSV = os.path.join(ROOT, r'04d_LR4\2. vosviewer\0.1a.Corpus_Merged-956 nos. v2.csv')
SS = os.path.join(ROOT, r'04d_LR4\5. SLR matrix\ss')
SCREEN = os.path.join(SS, 'screen')
os.makedirs(SCREEN, exist_ok=True)

def norm(s):
    s = unicodedata.normalize('NFKD', s or '')
    return re.sub(r'[^a-z0-9]', '', s.lower())

def clean(s):
    return re.sub(r'\s+', ' ', s or '').strip()

rows = []
with open(CSV, encoding='utf-8-sig', newline='') as f:
    rd = csv.DictReader(f)
    cols = rd.fieldnames
    n = 0
    for r in rd:
        n += 1
        yr = clean(r.get('Year', ''))
        m = re.search(r'\d{4}', yr)
        yr = m.group(0) if m else yr
        rows.append(dict(row=n,
                         authors=clean(r.get('Authors', '')),
                         title=clean(r.get('Title', '')),
                         year=yr,
                         journal=clean(r.get('Source title', '')),
                         doi=clean(r.get('DOI', '')),
                         abstract=clean(r.get('Abstract', '')),
                         kw=clean(r.get('Author Keywords', '')),
                         ikw=clean(r.get('Index Keywords', '')),
                         dtype=clean(r.get('Document Type', '')),
                         db=clean(r.get('Source', '')),
                         eid=clean(r.get('EID', '')),
                         link=clean(r.get('Link', ''))))

# ---- slug per record (first-author surname + year, dedup -a/-b...) ----
INITIAL_RE = re.compile(r'^[A-Za-z][A-Za-z]?\.?$')

def surname(aus):
    a = (aus.split(';')[0] if aus else '').strip()
    a = re.sub(r'[^A-Za-z\u00c0-\u024f\- ,.]', '', a).strip()
    if not a:
        return 'Anon'
    if ',' in a:
        a = a.split(',')[0].strip()
    toks = [t for t in a.split() if t]
    if not toks:
        return 'Anon'
    last = toks[-1]
    last_core = last.rstrip('.')
    # "Ullah F." / "Maté-González M.Á." -> last token is initials -> surname is previous
    if last != last_core or INITIAL_RE.match(last_core):
        if len(toks) >= 2:
            return toks[-2].rstrip('.')
        return last_core
    return last.rstrip('.')

slugs = {}
for rec in rows:
    base = surname(rec['authors']) + rec['year']
    i = 1
    cand = base
    while cand in slugs:
        cand = base + chr(96 + i)  # -a, -b, ...
        i += 1
    slugs[cand] = True
    rec['slug'] = cand

# ---- duplicate diagnostics ----
doi_counts = {}
tn_counts = {}
for rec in rows:
    if rec['doi']:
        doi_counts[rec['doi'].lower()] = doi_counts.get(rec['doi'].lower(), 0) + 1
    tn = norm(rec['title'])
    if len(tn) >= 25:
        tn_counts[tn] = tn_counts.get(tn, 0) + 1

dup_doi = sorted((v, k) for k, v in doi_counts.items() if v > 1)
dup_ti = sorted((v, k) for k, v in tn_counts.items() if v > 1)

with open(os.path.join(SS, 'corpus_lr4.json'), 'w', encoding='utf-8') as f:
    json.dump(rows, f, ensure_ascii=False, indent=1)

# ---- screening worksheet chunks (60 records each) ----
CH = 60
nchunks = (len(rows) + CH - 1) // CH
for ci in range(nchunks):
    sl = rows[ci * CH:(ci + 1) * CH]
    lines = []
    for rec in sl:
        ab = rec['abstract']
        ab = ab[:1000] + ('...' if len(ab) > 1000 else '')
        lines.append('##### R%s | %s | %s | %s | %s' % (
            rec['row'], rec['slug'], rec['year'], rec['db'][:12], rec['dtype']))
        lines.append('T: ' + rec['title'][:280])
        lines.append('J: ' + rec['journal'][:120])
        lines.append('A: ' + (ab or '(no abstract)'))
        lines.append('K: ' + rec['kw'][:160] + ' || ' + rec['ikw'][:160])
        lines.append('D: ' + rec['doi'])
        lines.append('')
    with open(os.path.join(SCREEN, 'chunk%02d.txt' % (ci + 1)), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

print('ROWS=%d | CHUNKS=%d' % (len(rows), nchunks))
print('COLUMNS=%d' % len(cols))
print('DUP_DOI_PAIRS=%d | DUP_TITLE_PAIRS=%d' % (len(dup_doi), len(dup_ti)))
print('NO_ABSTRACT=%d | NO_DOI=%d' % (
    sum(1 for r in rows if not r['abstract']), sum(1 for r in rows if not r['doi'])))
from collections import Counter
print('DOCTYPE:', dict(Counter(r['dtype'] for r in rows)))
print('SOURCE:', dict(Counter(r['db'] for r in rows)))
print('YEAR_RANGE:', min(int(r['year']) for r in rows if r['year'].isdigit()),
      '-', max(int(r['year']) for r in rows if r['year'].isdigit()))
