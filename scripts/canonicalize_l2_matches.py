# -*- coding: utf-8 -*-
"""Create canonical R### PDF copies for verified L2 noncanonical matches."""
import json
import os
import shutil

ROOT = r'h:\phd\6.pjt\LR1\papers'
L2 = os.path.join(ROOT, '04d_LR4', '4. fulltext L2')
SS = os.path.join(ROOT, '04d_LR4', '5. SLR matrix', 'ss')
MATCHES = os.path.join(SS, 'l2_noncanonical_matches.json')

# R226 is Step-1 Exclude; R616 already has a canonical active PDF/TXT.
SKIP_ROWS = {226, 616}

with open(MATCHES, encoding='utf-8') as fh:
    rows = json.load(fh)

copied = []
for row in rows:
    rid = row.get('row')
    if not rid or rid in SKIP_ROWS:
        continue
    if row.get('status') not in {'doi-match', 'title-match'}:
        continue
    src = os.path.join(L2, row['file'])
    dst = os.path.join(L2, row['suggested_name'])
    if os.path.exists(dst):
        print('exists', row['suggested_name'])
        continue
    shutil.copy2(src, dst)
    copied.append(row['suggested_name'])
    print('copied', row['file'], '->', row['suggested_name'])

print('copied_count', len(copied))