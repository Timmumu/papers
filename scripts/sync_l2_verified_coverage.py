# -*- coding: utf-8 -*-
"""Synchronize DOI/title verified L2 canonical PDFs into coverage_lr4.json."""
import json
import os

ROOT = r'h:\phd\6.pjt\LR1\papers'
L2 = os.path.join(ROOT, '04d_LR4', '4. fulltext L2')
TXT = os.path.join(L2, 'txt')
SS = os.path.join(ROOT, '04d_LR4', '5. SLR matrix', 'ss')
MATCHES = os.path.join(SS, 'l2_noncanonical_matches.json')
COVERAGE = os.path.join(SS, 'coverage_lr4.json')

with open(COVERAGE, encoding='utf-8') as fh:
    coverage = json.load(fh)
with open(MATCHES, encoding='utf-8') as fh:
    matches = json.load(fh)

EXTRAS = [
    {'row': 868, 'status': 'doi-match', 'suggested_name': 'R868_Song2023.pdf',
     'slug': 'Song2023', 'doi': '10.1002/rob.22127',
     'title': 'Digital twin-assisted fault diagnosis system for robot joints with insufficient data'},
]
matches = matches + EXTRAS

updated = []
for row in matches:
    rid = row.get('row')
    if not rid or row.get('status') not in {'doi-match', 'title-match'}:
        continue
    if rid == 226:
        continue
    pdf = os.path.join(L2, row['suggested_name'])
    txt = os.path.join(TXT, row['suggested_name'][:-4] + '.txt')
    if not (os.path.exists(pdf) and os.path.exists(txt) and os.path.getsize(txt) > 2000):
        continue
    key = str(rid)
    current = coverage.get(key, {})
    current.update({
        'slug': row.get('slug', current.get('slug', '')),
        'status': 'verified',
        'method': 'manual-l2-doi-title-match',
        'doi': row.get('doi', current.get('doi', '')),
        'title': row.get('title', current.get('title', '')),
        'pdf': pdf,
        'en_file': row['suggested_name'],
    })
    coverage[key] = current
    updated.append(rid)

with open(COVERAGE, 'w', encoding='utf-8') as fh:
    json.dump(coverage, fh, ensure_ascii=False, indent=1)

print('updated', len(updated), ','.join('R%03d' % rid for rid in sorted(updated)))