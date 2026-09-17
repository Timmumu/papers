# -*- coding: utf-8 -*-
"""Read specific snippets around integration mechanisms."""
import re, os

FT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'

def seg(base, a, b, label):
    c = open(os.path.join(FT, base + '.txt'), encoding='utf-8', errors='replace').read()
    print('=' * 100)
    print(label)
    print(c[a:b].replace('\n', ' '))
    print()

# Alvaro: how video and beacon data are related (timestamp/sync)
seg('3668_Alvaro2025', 11300, 12300, 'Alvaro sync/video integration')
seg('3668_Alvaro2025', 35000, 37300, 'Alvaro timestamps/Grafana')

# Araujo: RFID-BIM linkage
seg('4028_Araujo2025', 14300, 16500, 'Araujo RFID-BIM formwork')
seg('4028_Araujo2025', 19800, 21600, 'Araujo registration/integration')

# Aroquipa: LiDAR-BIM-model link
seg('3975_Aroquipa2025', 13400, 14500, 'Aroquipa LiDAR-BIM')
seg('3975_Aroquipa2025', 10000, 12000, 'Aroquipa BIM model pipeline')
