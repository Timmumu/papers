# -*- coding: utf-8 -*-
import os
FT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
def seg(base, a, b, label):
    c = open(os.path.join(FT, base + '.txt'), encoding='utf-8', errors='replace').read()
    print('=' * 100)
    print(label)
    print(c[a:b].replace('\n', ' ')[:900])
    print()
seg('3839_Li2023-pipeline', 3700, 4600, '3839 image context (method?)')
seg('3839_Li2023-pipeline', 42700, 43500, '3839 total station / validation')
seg('3839_Li2023-pipeline', 66000, 66900, '3839 fusion mentions (future work?)')
seg('3894_Lv2026-slope', 900, 2600, '3894 method intro')
seg('3894_Lv2026-slope', 3900, 4400, '3894 survey/img context')
seg('3965_Machado2025', 7400, 8400, '3965 image context')
seg('3986_Machado2024', 12000, 13700, '3986 image/photo context')
seg('3986_Machado2024', 45000, 46000, '3986 registration context')
seg('3559_Talmaki2022', 3000, 3600, '3559 image context')
