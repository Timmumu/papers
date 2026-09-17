# -*- coding: utf-8 -*-
"""Adjudication helper: for every non-verified LR4 include, print the paper
title and the top-5 filename candidates with hit counts, for manual review.

Usage: .venv\\Scripts\\python.exe scripts/adjudicate_lr4.py [limit]
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SS = os.path.join(ROOT, '04d_LR4', '5. SLR matrix', 'ss')
sys.path.insert(0, os.path.join(ROOT, 'scripts'))

import importlib.util
spec = importlib.util.spec_from_file_location('stage_lr4', os.path.join(ROOT, 'scripts', 'stage_fulltext_lr4.py'))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

from screening_data_lr4 import S4, decision

with open(os.path.join(SS, 'corpus_lr4.json'), encoding='utf-8') as f:
    CORPUS = json.load(f)
BYROW = {rec['row']: rec for rec in CORPUS}
INCLUDED = sorted(r for r, t in S4.items() if decision(t[:5]) == 'Include')

cov = json.load(open(os.path.join(SS, 'coverage_lr4.json'), encoding='utf-8'))
files = m.walk_pdfs()

limit = int(sys.argv[1]) if len(sys.argv) > 1 else 0
n = 0
for r in INCLUDED:
    v = cov.get(str(r), {})
    if v.get('status') == 'verified':
        continue
    rec = BYROW[r]
    cands = m.match_candidates(m.surname(rec['authors']), rec['year'], files, rec['authors'])
    ws = m.title_full(rec['title'])
    fh = []
    for path, base, yr in cands:
        low = m.strip_accents(base[:-4])
        hits = len([w for w in ws if w in low or w[:5] in low])
        yr_ok = rec['year'] in base or (rec['year'].isdigit() and any(str(int(rec['year']) + d) in base for d in (-1, 1)))
        fh.append((hits, yr_ok, base))
    fh.sort(key=lambda x: (-x[0], -int(x[1])))
    print('R%03d %-20s | %s' % (r, rec['slug'], rec['title'][:70]))
    for hits, yr_ok, base in fh[:5]:
        print('     %2d %s %s' % (hits, 'Y' if yr_ok else 'n', base[:75]))
    n += 1
    if limit and n >= limit:
        break
print('unresolved shown: %d' % n)
