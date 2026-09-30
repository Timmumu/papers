# -*- coding: utf-8 -*-
"""Validate PDFs in 04d_LR4/4. fulltext L2 against corpus metadata.
For each R###_slug.pdf: pypdf open, text head, check DOI or surname-year match.
Writes l2_validation.json.
"""
import json
import os
import re
import sys

sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
ROOT = r'h:\phd\6.pjt\LR1\papers'
L2 = os.path.join(ROOT, '04d_LR4', '4. fulltext L2')
SS = os.path.join(ROOT, '04d_LR4', '5. SLR matrix', 'ss')

from pypdf import PdfReader

miss = json.load(open(os.path.join(SS, 'missing_pdfs.json'), encoding='utf-8'))
byrow = {m['row']: m for m in miss}
out = []
for f in sorted(os.listdir(L2)):
    if not f.lower().endswith('.pdf'):
        continue
    m = re.match(r'R(\d+)_(.+)\.pdf$', f)
    if not m:
        out.append({'file': f, 'status': 'skip-noncanonical'})
        continue
    r = int(m.group(1))
    meta = byrow.get(r)
    if not meta:
        out.append({'file': f, 'status': 'not-in-missing-list'})
        continue
    p = os.path.join(L2, f)
    try:
        rd = PdfReader(p)
        head = ' '.join((pg.extract_text() or '') for pg in rd.pages[:2])
        head = re.sub(r'\s+', ' ', head)[:2000].lower()
        doi_norm = meta['doi'].lower()
        doi_hit = doi_norm in head or doi_norm.replace('https://doi.org/', '') in head
        surname = meta['slug']
        # first surname token (strip trailing digits/letters suffix)
        sur = re.match(r'^(.+?)(?:[0-9]+[a-z]?)?$', surname).group(1)
        sur = re.sub(r'[^a-z]', '', sur.lower())
        name_hit = len(sur) >= 4 and sur[:6] in head
        ok = bool(doi_hit or name_hit)
        status = 'ok' if ok else 'suspect'
        out.append({'file': f, 'row': r, 'status': status, 'pages': len(rd.pages),
                    'doi_hit': doi_hit, 'name_hit': name_hit,
                    'head': head[:160]})
    except Exception as e:
        out.append({'file': f, 'row': r, 'status': 'broken', 'err': str(e)[:100]})

json.dump(out, open(os.path.join(SS, 'l2_validation.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
from collections import Counter
print(Counter(o['status'] for o in out))
for o in out:
    if o['status'] != 'ok':
        print(o['file'], o['status'], (o.get('err') or o.get('head') or '')[:120])
