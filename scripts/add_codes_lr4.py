# -*- coding: utf-8 -*-
"""Merge code_add_lr4.ADD/AH2/AI2/FD2/FDEV2/FDCF2 into the LR4 step-3 stores
and rewrite the store modules. Idempotent.

Usage: .venv\\Scripts\\python.exe scripts/add_codes_lr4.py
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))

import step3_lr4_data, step3_lr4_extra, step3_lr4_fusion
import code_add_lr4

S3L = step3_lr4_data.S3L
AH = step3_lr4_extra.AH
AI = step3_lr4_extra.AI
FD = step3_lr4_fusion.FD
FDEV = step3_lr4_fusion.FDEV
FDCF = step3_lr4_fusion.FDCF

for r, v in code_add_lr4.ADD.items():
    assert len(v) == 16, (r, len(v))
    S3L[r] = tuple(v)
for r, v in code_add_lr4.AH2.items():
    AH[r] = v
for r, v in code_add_lr4.AI2.items():
    AI[r] = v
for r, v in code_add_lr4.FD2.items():
    FD[r] = v
for r, v in code_add_lr4.FDEV2.items():
    FDEV[r] = v
for r, v in code_add_lr4.FDCF2.items():
    FDCF[r] = v


def dump(path, lines):
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')


dump(os.path.join(ROOT, 'scripts', 'step3_lr4_data.py'), [
    '# -*- coding: utf-8 -*-',
    '"""LR4 Step-3 deep-read codes for included papers (Prompt B).',
    'Keyed by corpus row r (1..956). Value tuple:',
    '(P, Q, R, U-Tier, V, W, X, Z-DfX, AA-selfimprove, AB-method, AC-modality,',
    ' AD-validation, AE-QA, AF-cluster, AG-key evidence[, SRC-fulltext-source]).',
    'Only papers with P=Q=R=Yes get full codes. Otherwise P/Q/R recorded, rest blank.',
    '16th element (optional) = full-text source label.',
    '"""',
    'S3L = {',
] + ['%d: %r,' % (r, S3L[r]) for r in sorted(S3L)] + ['}', ''])

dump(os.path.join(ROOT, 'scripts', 'step3_lr4_extra.py'), [
    '# -*- coding: utf-8 -*-',
    '"""LR4 AH (strength & gap filled) and AI (deficiencies & future work) for',
    'the full-coded Step-3 papers. Keyed by corpus row r."""',
    '', 'AH = {',
] + ['%d: %r,' % (r, AH[r]) for r in sorted(AH)] + ['}', '', 'AI = {',
] + ['%d: %r,' % (r, AI[r]) for r in sorted(AI)] + ['}', ''])

dump(os.path.join(ROOT, 'scripts', 'step3_lr4_fusion.py'), [
    '# -*- coding: utf-8 -*-',
    '"""LR4 fusion-depth coding (after AC data modality).',
    'FD: Co-present | Aligned | Fused | SINGLE | Unclear; FDEV: evidence;',
    'FDCF: High | Medium | Low. Keyed by corpus row r."""',
    '', 'FD = {',
] + ['%d: %r,' % (r, FD[r]) for r in sorted(FD)] + ['}', '', 'FDEV = {',
] + ['%d: %r,' % (r, FDEV[r]) for r in sorted(FDEV)] + ['}', '', 'FDCF = {',
] + ['%d: %r,' % (r, FDCF[r]) for r in sorted(FDCF)] + ['}', ''])

print('merged: %d new codes | stores now: S3L=%d AH=%d AI=%d FD=%d' % (
    len(code_add_lr4.ADD), len(S3L), len(AH), len(AI), len(FD)))
