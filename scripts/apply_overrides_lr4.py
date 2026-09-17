# -*- coding: utf-8 -*-
"""Apply manual adjudication overrides: rows whose Endnote filename matches
the paper title verbatim but failed automated gates. Copies PDF to the LR4
staging folder and marks coverage verified (method 'manual').

Usage: .venv\\Scripts\\python.exe scripts/apply_overrides_lr4.py
"""
import json
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SS = os.path.join(ROOT, '04d_LR4', '5. SLR matrix', 'ss')
FT1 = os.path.join(ROOT, '04d_LR4', '3. fulltext L1')
EN_PDF = r'H:\phd\paper\Endnote\My EndNote Library.Data\PDF'

sys.path.insert(0, os.path.join(ROOT, 'scripts'))

# row -> exact Endnote basename (must exist in the library)
OVERRIDES = {
    26: 'Han-2026-Construction Path of Shanghai Orienta.pdf',
    87: 'Yan-2026-Digital twin-enabled 3D near-misses p.pdf',
    88: 'Sun-2025-Digital twin of advanced geological c.pdf',
    107: 'Guo-2026-AN INTELLIGENT CONSTRUCTION SYSTEM BA.pdf',
    111: 'Shen-2026-Reverse digital twin mapping of buil.pdf',
    143: 'Yang-2026-Digital twin-based framework for mul.pdf',
    145: 'Zhang-2026-Digital twin-enabled synchronous ja.pdf',
    146: 'Shi-2026-The Research on the Construction Meth.pdf',
    147: 'Guo-2025-A methodology for sky-space-ground in.pdf',
    154: 'Zhao-2026-Digital twin-enabled simulation syst.pdf',
    169: 'Pérez Pérez-2026-ESTIMATING THE SERVICE LIFE O.pdf',
    172: 'Wang-2026-A Partially Validated Probabilistic.pdf',
    217: 'Shariatfar-2026-When Roads Go Underwater_ AI-E.pdf',
    219: 'Chang-2026-A transformer-based surrogate model.pdf',
    238: 'Liu-2026-Multi-line LiDAR 3D construction envi.pdf',
    260: 'Su-2025-Development of a digital twin-driven b.pdf',
    278: 'Zhang-2025-Digital Safety Navigation for Tower.pdf',
    292: 'Tang-2025-Digital twin-enabled deep learning f.pdf',
    356: 'Yu-2025-Scenario Modeling for Urban Road Emerg.pdf',
    379: 'Zhang-2025-Research on the Digital Twin System.pdf',
    381: 'Song-2026-Simultaneous Digital Twin_ Chaining.pdf',
    400: 'Lv-2026-Automating digitalization of engineere.pdf',
    405: 'Xiong-2026-Edge-cloud collaborative digital tw.pdf',
    413: 'Han-2026-Digital twin-driven pose estimation a.pdf',
    416: 'Wang-2025-Digital twin safety analysis of larg.pdf',
    417: 'Wu-2026-Knowledge-data driven digital twin pla.pdf',
    465: 'Xie-2025-AIoT-powered building digital twin fo.pdf',
    468: 'Yan-2025-Real-Time Digital Twin-Driven 3D Near.pdf',
    504: 'Liu-2023-Multisensory and BIM-Integrated Digit.pdf',
    537: 'Hong-2022-An Integrated Intelligent Approach f.pdf',
    550: 'Liu-2020-Intelligent tensioning method for pre.pdf',
    551: 'Hu-2024-An intelligent BIM-enabled digital twi.pdf',
    569: 'He-2024-Reliable simulation analysis for high-.pdf',
    573: 'Jiang-2023-Intelligent control of building fir.pdf',
    599: 'Wang-2024-Development and validation of graphi.pdf',
    622: 'Kaewunruen-2021-Digital Twin Aided Vulnerabili.pdf',
    625: 'Fang-2023-Intervention and management of const.pdf',
    630: 'Zhao-2024-Predictive diagnosis of hidden risk.pdf',
    666: 'Zhang-2024-Joint detection PCD-based method fo.pdf',
    677: 'Sresakoolchai-2023-Railway infrastructure main.pdf',
    704: 'Liu-2025-Structural safety risk prediction met.pdf',
    722: 'Zhao-2025-Digital twin-enabled anti-collision.pdf',
    731: 'Zeng-2025-A dynamic digital twin-based health.pdf',
    753: 'Zhang-2022-Digital Twins for Construction Site.pdf',
    758: 'Lai-2022-Building a Lightweight Digital Twin o.pdf',
    772: 'Zhu-2022-Intelligent Prediction of Prestressed.pdf',
    774: 'Shi-2024-Optimization method of cable structur.pdf',
    791: 'Zhao-2022-An Established Theory of Digital Twi.pdf',
    812: 'Yu-2024-Intelligent Analysis of Construction S.pdf',
    813: 'Ye-2023-A digital twin approach for tunnel con.pdf',
    847: 'Wang-2024-Enabling Building Information Model-.pdf',
    876: 'Tran-2025-Physical digital twins for ancient s.pdf',
    886: 'Sun-2023-Intelligent Risk Prognosis and Contro.pdf',
    895: 'Jiang-2024-Early-warning of unsafe hoisting op.pdf',
    904: 'Lin-2026-Creation and application of a geometr.pdf',
    914: 'Deng-2025-Structural Analysis of Construction.pdf',
    919: 'Wang-2021-Interactive and Immersive Process-Le.pdf',
    925: 'Zhang-2025-Advancements in digital twin-enhanc.pdf',
    927: 'Tian-2026-Defect Trigger Identification in a C.pdf',
    942: 'Geng-2025-Integrating multi-source data for li.pdf',
}

# locate Endnote paths by basename
paths = {}
for root, _, files in os.walk(EN_PDF):
    for f in files:
        if f.lower().endswith('.pdf'):
            paths.setdefault(f, os.path.join(root, f))

with open(os.path.join(SS, 'corpus_lr4.json'), encoding='utf-8') as fh:
    CORPUS = json.load(fh)
BYROW = {rec['row']: rec for rec in CORPUS}

cov = json.load(open(os.path.join(SS, 'coverage_lr4.json'), encoding='utf-8'))
ok = fail = 0
for r, base in OVERRIDES.items():
    src = paths.get(base)
    if not src:
        print('R%03d MISSING source file: %s' % (r, base))
        fail += 1
        continue
    rec = BYROW[r]
    dst = os.path.join(FT1, 'R%03d_%s.pdf' % (r, rec['slug']))
    shutil.copy2(src, dst)
    cov[str(r)] = {'slug': rec['slug'], 'pdf': dst, 'en_file': base,
                   'status': 'verified', 'method': 'manual-fname',
                   'doi': rec['doi'], 'title': rec['title'][:90]}
    ok += 1
    print('R%03d %-18s <- %s' % (r, rec['slug'], base[:60]))

json.dump(cov, open(os.path.join(SS, 'coverage_lr4.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print('overrides applied: %d ok, %d fail' % (ok, fail))
