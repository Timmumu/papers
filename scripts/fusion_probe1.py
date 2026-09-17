# -*- coding: utf-8 -*-
"""Extract data-integration evidence from 5 fulltexts for Fusion-depth coding."""
import re, os

FT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
papers = [
    ('3668_Alvaro2025', ['synchron', 'timestamp', 'register', 'align', 'grafana', 'video', 'beacon', 'fused', 'combine']),
    ('4028_Araujo2025', ['RFID', 'BIM', 'object', 'tag', 'identifier', 'link', 'register', 'integration', 'formwork']),
    ('3828_Arhrib2026', ['anchor', 'georeferenc', 'raycast', 'register', 'coordinate', 'frustum', 'PostGIS', 'defect']),
    ('3662_Armijo2024', ['acceler', 'vibration', 'sensor', 'strain', 'fuse', 'combine', 'multi']),
    ('3975_Aroquipa2025', ['LiDAR', 'BIM', 'SAP2000', '3DEC', 'geometry', 'modal', 'register', 'align', 'model']),
]
for base, kws in papers:
    p = os.path.join(FT, base + '.txt')
    if not os.path.exists(p):
        print('MISSING', p)
        continue
    c = open(p, encoding='utf-8', errors='replace').read()
    print('=' * 100)
    print(base, '| len', len(c))
    for kw in kws:
        idxs = [m.start() for m in re.finditer(kw, c, re.I)]
        print(f'  [{kw}] {len(idxs)} hits, first at {idxs[:3]}')
