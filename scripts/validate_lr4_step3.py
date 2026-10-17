# -*- coding: utf-8 -*-
"""LR4 Step-3 validator: schema checks over S3L / AH / AI / FD / FDEV / FDCF
and cross-store reconciliation with coverage_lr4.json.

Usage: .venv\\Scripts\\python.exe scripts/validate_lr4_step3.py
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SS = os.path.join(ROOT, '04d_LR4', '5. SLR matrix', 'ss')
sys.path.insert(0, os.path.join(ROOT, 'scripts'))

import step3_lr4_data, step3_lr4_extra, step3_lr4_fusion
from screening_data_lr4 import S4, decision

S3L = step3_lr4_data.S3L
AH = step3_lr4_extra.AH
AI = step3_lr4_extra.AI
FD = step3_lr4_fusion.FD
FDEV = step3_lr4_fusion.FDEV
FDCF = step3_lr4_fusion.FDCF

INCLUDED = sorted(r for r, t in S4.items() if decision(t[:5]) == 'Include')

TIERS = {
    'Tier 1 - Digital Model (static, no live data)',
    'Tier 2 - Digital Shadow (one-way physical to virtual)',
    'Tier 3 - Digital Twin (bidirectional, two-way)',
    'Tier 4 - Cognitive / Self-improving',
    'Unclear',
}
DFX = {'Design for Safety (DfS)', 'Other'}
AA = {'None', 'Mentioned only', 'Implemented', 'Convergence-characterised'}
AB = {
    'Computer Vision / CNN / object-detection', 'Perception / Computer Vision',
    'Graph Neural Network (GNN)',
    'LSTM / RNN (recurrent networks)', 'Transformer / Large Language Model (LLM)',
    'Reinforcement Learning (RL)', 'Bayesian / probabilistic',
    'Agent-based model (ABM)', 'Finite Element Method / physics-based',
    'Ontology / semantic', 'Statistical / change-point',
    'Digital Twin platform (no machine learning)', 'Other / Mixed',
}
AC = {'Single (one data type)', 'Multi (two or more data types)'}
AD = {'Conceptual (no test)', 'Simulation', 'Single case study',
      'Cross-project (multiple real projects)'}
FDC = {'Co-present', 'Aligned', 'Fused', 'SINGLE', 'Unclear'}
FCF = {'High', 'Medium', 'Low'}

errs = []
full = [r for r in INCLUDED if r in S3L and S3L[r][0] == 'Yes' and S3L[r][1] == 'Yes' and S3L[r][2] == 'Yes']
excl = [r for r in INCLUDED if r in S3L and r not in full]

# coded rows must be included rows
for r in S3L:
    if r not in INCLUDED:
        errs.append('row %d coded but not a Step-1 include' % r)

for r in sorted(S3L):
    v = S3L[r]
    if len(v) < 15:
        errs.append('row %d tuple too short (%d)' % (r, len(v)))
        continue
    P, Q, R = v[0], v[1], v[2]
    for tag, val in (('P', P), ('Q', Q), ('R', R)):
        if val not in ('Yes', 'No'):
            errs.append('row %d %s=%r invalid' % (r, tag, val))
    if r in full:
        if v[3] not in TIERS:
            errs.append('row %d U tier invalid: %r' % (r, v[3]))
        for tag, val in (('V', v[4]), ('W', v[5]), ('X', v[6])):
            if val not in (0, 1, '0', '1'):
                errs.append('row %d %s=%r invalid' % (r, tag, val))
        if v[7] not in DFX:
            errs.append('row %d Z invalid: %r' % (r, v[7]))
        if v[8] not in AA:
            errs.append('row %d AA invalid: %r' % (r, v[8]))
        if v[9] not in AB:
            errs.append('row %d AB invalid: %r' % (r, v[9]))
        if v[10] not in AC:
            errs.append('row %d AC invalid: %r' % (r, v[10]))
        if v[11] not in AD:
            errs.append('row %d AD invalid: %r' % (r, v[11]))
        if not (isinstance(v[12], int) and 0 <= v[12] <= 5):
            errs.append('row %d AE=%r invalid' % (r, v[12]))
        if not v[14]:
            errs.append('row %d AG empty' % r)
        if r not in FD or r not in FDEV or r not in FDCF:
            errs.append('row %d missing fusion trio' % r)
        else:
            if FD[r] not in FDC:
                errs.append('row %d FD invalid: %r' % (r, FD[r]))
            if FDCF[r] not in FCF:
                errs.append('row %d FDCF invalid: %r' % (r, FDCF[r]))
            if not FDEV[r]:
                errs.append('row %d FDEV empty' % r)
        if r not in AH or not AH[r] or r not in AI or not AI[r]:
            errs.append('row %d missing AH/AI' % r)
    else:
        for tag, val in (('U', v[3]), ('Z', v[7])):
            if val not in ('', None):
                errs.append('row %d Stage-2 excl but %s non-empty: %r' % (r, tag, val))
        if not v[14]:
            errs.append('row %d Stage-2 excl but AG (reason) empty' % r)

# coverage reconciliation
covp = os.path.join(SS, 'coverage_lr4.json')
if os.path.exists(covp):
    cov = json.load(open(covp, encoding='utf-8'))
    for r in full:
        v = cov.get(str(r), {})
        if v.get('status') != 'verified':
            errs.append('row %d full-coded but fulltext not verified (%s)' % (r, v.get('status', 'no entry')))

print('coded=%d full=%d stage2-excl=%d' % (len(S3L), len(full), len(excl)))
if errs:
    print('ERRORS (%d):' % len(errs))
    for e in errs[:60]:
        print(' -', e)
else:
    print('VALIDATION OK')
