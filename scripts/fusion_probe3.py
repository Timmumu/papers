# -*- coding: utf-8 -*-
"""Probe 5 ambiguous papers for their actual measured data types."""
import os, re, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from screening_data import S

FT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
TERMS = {
    'rgb/image/camera/photo': r'rgb|image|camera|photogram|vision|video|uav|drone',
    'lidar/scan/point': r'lidar|laser scan|point cloud|pcd',
    'total station': r'total station',
    'sensor(s)': r'sensor',
    'questionnaire/survey': r'questionnaire|survey|interview',
    'fuse/fusion': r'fus(e|ed|ion)',
    'combine/joint': r'combin|jointly|integrat',
    'register/align': r'register|align|georeferenc|coordinat',
}
for n, slug in [(3839, 'Li2023-pipeline'), (3894, 'Lv2026-slope'), (3965, 'Machado2025'), (3986, 'Machado2024'), (3559, 'Talmaki2022')]:
    p = os.path.join(FT, '%d_%s.txt' % (n, slug))
    print('=' * 100)
    print(n, slug, '| exists:', os.path.exists(p))
    if not os.path.exists(p):
        continue
    c = open(p, encoding='utf-8', errors='replace').read()
    print('len', len(c))
    for k, pat in TERMS.items():
        hits = [m.start() for m in re.finditer(pat, c, re.I)]
        print('  [%s] %d hits, first at %s' % (k, len(hits), hits[:5]))
