# -*- coding: utf-8 -*-
"""Resolve LR4 fulltext gaps using 04c's staged fulltext-level1 txt files.

For every LR4 include whose coverage status is 'unverified' or 'no-candidate',
look up its DOI (then title) against the 04c corpus + coverage_match.json,
and copy the matched 04c txt into the LR4 txt staging folder.

Usage: .venv\\Scripts\\python.exe scripts/resolve_lr4_via_04c.py
"""
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SS = os.path.join(ROOT, '04d_LR4', '5. SLR matrix', 'ss')
FT1 = os.path.join(ROOT, '04d_LR4', '3. fulltext L1')
TXT_DIR = os.path.join(FT1, 'txt')
FT_C = os.path.join(ROOT, '04c_LR 3round', '3. fulltext-level1')
COV = os.path.join(SS, 'coverage_lr4.json')
RIS = os.path.join(ROOT, '04c_LR 3round', '429 papers.txt')
MATCH_C = os.path.join(ROOT, '04c_LR 3round', 'ss', 'coverage_match.json')

sys.path.insert(0, os.path.join(ROOT, 'scripts'))
from screening_data_lr4 import S4, decision  # noqa: E402

with open(os.path.join(SS, 'corpus_lr4.json'), encoding='utf-8') as f:
    CORPUS = json.load(f)
BYROW = {rec['row']: rec for rec in CORPUS}
INCLUDED = sorted(r for r, t in S4.items() if decision(t[:5]) == 'Include')
cov = json.load(open(COV, encoding='utf-8'))


def norm(s):
    return re.sub(r'[^a-z0-9]', '', (s or '').lower())


def norm_doi(d):
    d = norm(d)
    return d[2:] if d.startswith('10') and len(d) > 10 else d


# ---- 04c: id -> (doi, title, first-author) + file from coverage_match ----
txt4 = open(RIS, encoding='utf-8', errors='replace').read()
recs = re.split(r'\nER  -\s*\n', txt4)
meta4 = {}
for r in recs:
    if 'TY  -' not in r:
        continue
    def field(tag):
        m = re.search(rf'^{tag}  - (.*?)(?=^[A-Z0-9]{{2}}  - |\Z)', r, re.M | re.S)
        return ' '.join(m.group(1).split()) if m else ''
    meta4[field('ID')] = dict(doi=field('DO'), ti=field('TI'))
m4 = json.load(open(MATCH_C, encoding='utf-8'))

doi4 = {}
for rid, info in m4.items():
    fname = info.get('file', '')
    if not fname or not os.path.exists(os.path.join(FT_C, fname)):
        continue
    md = meta4.get(rid, {})
    if md.get('doi'):
        doi4[norm_doi(md['doi'])] = fname

# title-index of 04c staged files (for DOI-less matches): file stem contains slug
print('04c staged txt available:', len(doi4))

done = fail = 0
for r in INCLUDED:
    key = str(r)
    v = cov.get(key)
    if not v or v.get('status') == 'verified':
        continue
    rec = BYROW[r]
    fname = None
    how = ''
    if rec['doi']:
        fname = doi4.get(norm_doi(rec['doi']))
        if fname:
            how = 'doi'
    if not fname:
        # title-signature against 04c file stems
        words = [w for w in re.split(r'\W+', rec['title'].lower()) if len(w) > 4][:6]
        for rid, info in m4.items():
            fn = info.get('file', '')
            if not fn or not os.path.exists(os.path.join(FT_C, fn)):
                continue
            stem = fn[:-4].lower()
            if sum(1 for w in words if w in stem) >= 5:
                fname = fn
                how = 'title-stem'
                break
    if not fname:
        fail += 1
        continue
    src = os.path.join(FT_C, fname)
    content = open(src, encoding='utf-8', errors='replace').read()[:20000].lower()
    if how == 'title-stem':
        words = [w for w in re.split(r'\W+', rec['title'].lower()) if len(w) > 4][:6]
        if sum(1 for w in words if w in content[:4000]) < 5:
            fail += 1
            continue
        how = 'title-content'
        # DOI match: verify the file actually contains the paper
        dn = norm_doi(rec['doi'])
        if not (len(dn) >= 12 and dn in re.sub(r'[^a-z0-9]', '', content)):
            # fall back to title signature
            words = [w for w in re.split(r'\W+', rec['title'].lower()) if len(w) > 4][:6]
            if sum(1 for w in words if w in content[:4000]) < 4:
                fail += 1
                continue
            how = 'title-content'
    dst = os.path.join(TXT_DIR, 'R%03d_%s.txt' % (r, rec['slug']))
    shutil.copy2(src, dst)
    v['status'] = 'verified'
    v['method'] = '04c-' + how
    v['en_file'] = fname
    v['txt'] = dst
    done += 1
    print('R%03d %-18s <- 04c [%s] %s' % (r, rec['slug'], how, fname))

json.dump(cov, open(COV, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('resolved via 04c: %d | still unresolved: %d' % (done, fail))
