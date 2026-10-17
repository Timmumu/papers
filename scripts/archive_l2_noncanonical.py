# -*- coding: utf-8 -*-
"""Archive noncanonical L2 originals after canonical R### copies exist.

Moves (never deletes) the original publisher-named PDFs whose canonical
R###_slug.pdf copies are already in place, so the L2 root shows canonical
names only. Files with no canonical target stay untouched.
"""
import json
import os
import re
import shutil

ROOT = r'h:\phd\6.pjt\LR1\papers'
L2 = os.path.join(ROOT, '04d_LR4', '4. fulltext L2')
SS = os.path.join(ROOT, '04d_LR4', '5. SLR matrix', 'ss')
KEPT = os.path.join(L2, '_kept_noncanonical_originals')
MATCHES = os.path.join(SS, 'l2_noncanonical_matches.json')

CANONICAL = re.compile(r'^R\d{3}_[A-Za-z0-9-]+\.pdf$')

with open(MATCHES, encoding='utf-8') as fh:
    matches = json.load(fh)
by_file = {row['file']: row for row in matches}

os.makedirs(KEPT, exist_ok=True)
moved, left = [], []

for name in sorted(os.listdir(L2)):
    if not name.lower().endswith('.pdf'):
        continue
    src = os.path.join(L2, name)

    # unlocked duplicate of the canonical R245 (canonical now holds same content)
    if name == 'R245_Kubota2026_unlocked.pdf' and os.path.exists(os.path.join(L2, 'R245_Kubota2026.pdf')):
        shutil.move(src, os.path.join(KEPT, name))
        moved.append(name)
        continue

    if CANONICAL.match(name):
        continue

    row = by_file.get(name)
    if row and row.get('status') in {'doi-match', 'title-match'} and row.get('row') not in (226,):
        target = os.path.join(L2, row['suggested_name'])
        if os.path.exists(target):
            shutil.move(src, os.path.join(KEPT, name))
            moved.append(name)
            continue
    left.append(name)

print('moved %d -> %s' % (len(moved), KEPT))
for name in moved:
    print('  +', name)
print('left in place %d' % len(left))
for name in left:
    print('  -', name)
