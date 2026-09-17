# -*- coding: utf-8 -*-
"""List remaining fusion-coding targets: index, rid, slug, AC, tier."""
import os, re, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
import step3_data, step3_fusion
from screening_data import S

RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
ris = open(RIS, encoding='utf-8', errors='replace').read()

def meta_for(rid):
    # find author/year/title block for rid
    for m in re.finditer(r'TY  - .*?ER  -', ris, re.S):
        blk = m.group(0)
        ids = re.findall(r'^ID  - (\d+)', blk, re.M)
        if str(rid) in ids:
            t = re.findall(r'^T1  - (.+)', blk, re.M)
            a = re.findall(r'^A1  - (.+)', blk, re.M)
            y = re.findall(r'^Y1  - (\d{4})', blk, re.M)
            return (t[0][:60] if t else '', a[0] if a else '', y[0] if y else '')
    return ('', '', '')

# rid mapping: screening index -> rid via step3_data S3 tuple? S3 values hold P..AG; rid comes from RIS 'ID'
# Rebuild script builds meta keyed by index; replicate simply: assume mapping dict exists in rebuild script
import importlib
rb = importlib.import_module('rebuild_step3_matrix')
meta = rb.meta
S3 = step3_data.S3
full = [n for n in S3 if tuple(S3[n][0:3]) == ('Yes','Yes','Yes')]
done = sorted(step3_fusion.FD)
todo = [n for n in full if n not in done]
print('full-coded:', len(full), '| done:', len(done), '| todo:', len(todo))
for n in sorted(todo):
    v = S3[n]
    m = meta.get(n, {})
    print('%3d | %s | %-22s | AC=%s | tier=%s' % (n, m.get('rid',''), m.get('author','')[:20], v[10], v[3][:12]))
