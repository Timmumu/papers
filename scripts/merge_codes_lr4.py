# -*- coding: utf-8 -*-
"""Merge a pending code module (code_add_lr4_b*.py) into the LR4 step-3 stores
and rewrite the store modules. Idempotent.
Usage: .venv\\Scripts\\python.exe scripts/merge_codes_lr4.py code_add_lr4_b2
"""
import importlib
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))

import step3_lr4_data, step3_lr4_extra, step3_lr4_fusion  # noqa: E402

modname = sys.argv[1]
mod = importlib.import_module(modname)

S3L = step3_lr4_data.S3L
AH = step3_lr4_extra.AH
AI = step3_lr4_extra.AI
FD = step3_lr4_fusion.FD
FDEV = step3_lr4_fusion.FDEV
FDCF = step3_lr4_fusion.FDCF

ADD = getattr(mod, 'ADD', {})
AH2 = getattr(mod, 'AH2', {})
AI2 = getattr(mod, 'AI2', {})
FD2 = getattr(mod, 'FD2', {})
FDEV2 = getattr(mod, 'FDEV2', {})
FDCF2 = getattr(mod, 'FDCF2', {})

for r, v in ADD.items():
    assert len(v) == 16, (r, len(v))
    S3L[r] = tuple(v)
AH.update(AH2)
AI.update(AI2)
FD.update(FD2)
FDEV.update(FDEV2)
FDCF.update(FDCF2)


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

print('merged %d new codes from %s | stores now: S3L=%d AH=%d AI=%d FD=%d' % (
    len(ADD), modname, len(S3L), len(AH), len(AI), len(FD)))
