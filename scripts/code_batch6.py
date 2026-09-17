# -*- coding: utf-8 -*-
"""Append S3 entries for the 4 newly recovered papers (42, 121, 122, 125),
append Step-3 sections to their atomic notes, rebuild matrix, verify."""
import os, re, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')

DATA = r'h:\phd\6.pjt\LR1\papers\scripts\step3_data.py'
OUT = r'h:\phd\6.pjt\LR1\papers\01_source_3rd_SLR'

import step3_data
from screening_data import S
S3 = step3_data.S3

ENTRIES = {
42: ('Yes','Yes','Yes','Tier 1 - Digital Model (static, no live data)',0,0,1,
     'Design for Safety (DfS)','None','Other / Mixed','Single (one data type)','Simulation',3,'Design for Safety',
     'AI-based ANN surrogate model for DTs in SHM of reinforced concrete bridges (Cervenka Consulting/CTU, RILEM SSCS 2025): ANN has two roles - calibrating the virtual twin to physical structure behavior, then deployment as fast-response surrogate providing safety information for ongoing SHM; physically informed deep learning trained from nonlinear FEM (ATENA) sensitivity analyses; demonstrated on Leonhardt shear-beam numerical example (100/400/1000-sample datasets) identifying material parameters (fc, ft, E, GF) from load-displacement diagrams. Numerical example only - no live data link to a real bridge, no actuation, no learning loop.',
     'Endnote'),
121: ('Yes','Yes','Yes','Tier 2 - Digital Shadow (one-way physical to virtual)',0,1,0,
     'Design for Safety (DfS)','None','Other / Mixed','Multi (two or more data types)','Single case study',4,'BIM-to-Digital-Twin architecture',
     'Integrated intelligent approach for monitoring and management of deep foundation pit in a subway station (Shenzhen Metro Line 12 Waterlands Resort East Station): on-site geological investigation + 3D transparent geology on BIM platform; multi-source sensing (MEMS, BOFDA distributed optical fiber, laser radar, UAV, machine vision) for pit axial force/displacement/strain/temperature; BIM-based intelligent monitoring platform (proprietary cast modeling cloud platform); four ML neural networks predict key pit parameters - GA-BP achieved smallest error on this project; DT app terminal with 3D visualization, full-lifecycle monitoring, predictive analysis + AR combining BIM 3D model with real tunnel scenario. One-way monitoring to prediction to risk management; no actuation, no learning loop.',
     'Endnote'),
122: ('Yes','Yes','Yes','Tier 2 - Digital Shadow (one-way physical to virtual)',0,1,0,
     'Design for Safety (DfS)','None','Digital Twin platform (no machine learning)','Single (one data type)','Single case study',4,'Design for Safety',
     'Digital construction site layout planning and real-time trajectory analysis for proactive safety monitoring and control of struck-by hazards (DTCS Right-time Analysis and Mitigation module; DTU/TUM): RTK-GNSS + LoRa live location tracking of pedestrian workers and heavy equipment streamed to DTCS; semi-static and dynamic hazard zones (1-m boundary + operator blind-space geometry); real-time incident detection of unauthorized entry and too-close proximity; density maps / histogram heatmaps identify hazardous activities; safety-plan revision recommendations (separating worker/equipment areas, temporary pedestrian walkways); field experiments in Munich subway rail maintenance staging area showed significant reduction in spatial conflicts and improved zone connectivity, with newly detected hazards (rail traffic, delivery trucks) triggering iterative plan updates. One-way monitoring to analysis to mitigation recommendations/alerts for safety personnel; no actuation, no learning loop.',
     'Endnote'),
125: ('Yes','Yes','Yes','Unclear',0,1,0,
     'Design for Safety (DfS)','None','Other / Mixed','Single (one data type)','Single case study',4,'Lifecycle / governance',
     'Multi-dimensional framework for assessing construction machinery digital twin (CMDT) maturity (HUST): 24 maturity indicators across five dimensions from literature review + expert interviews; expert-opinion grouping via community detection with competency/quality-weighted groups; improved bi-objective optimization model (adjustable penalty weight balancing PDF overlap vs confidence of collective opinion) aggregates expert judgments into overall CMDT maturity; validated on a real-world DT-driven ACS (automated climbing system) high-rise project whose DT integrates safety sensors (inclinometers, leveling instruments) and operational sensors (oil pressure, laser rangefinders); identifies maturity levels and improvement pathways. Study assesses DT maturity - does not itself build/operate a DT (tier Unclear); no learning loop.',
     'Endnote'),
}

missing = [n for n in ENTRIES if n in S3]
print('already coded (skip):', missing)
for n in ENTRIES:
    if n in S3:
        continue
    S3[n] = ENTRIES[n]
    print('added S3[%d] %s' % (n, S[n][7]))

# regenerate data file preserving comments
src = open(DATA, encoding='utf-8').read()
comment_of = {}
for n in S3:
    m = re.search(r'\n([ \t]*#(?:[^\n]*))\nS3\[%d\]' % n, src)
    if m:
        comment_of[n] = m.group(1)
# add a batch comment for the new ones
for n in ENTRIES:
    if n not in comment_of:
        comment_of[n] = f'# Batch 6 - Endnote upload {n}'
header = '''"""Step-3 deep-read codes for included papers.

Keyed by paper index n (1-429). Value tuple:
(P, Q, R, U-Tier, V, W, X, Z-DfX, AA-selfimprove, AB-method, AC-modality,
 AD-validation, AE-QA, AF-cluster, AG-key evidence[, SRC-fulltext-source])

Only papers with P=Q=R=Yes get full codes. Otherwise P/Q/R recorded, rest blank.
16th element (optional) = full-text source label (e.g. 'Endnote').
"""
S3 = {}
'''
lines = [header]
for n in sorted(S3):
    lines.append(comment_of.get(n, '# Batch'))
    lines.append('S3[%d] = (%s)' % (n, ', '.join(repr(x) for x in S3[n])))
    lines.append('')
open(DATA, 'w', encoding='utf-8').write('\n'.join(lines))
print('data file regenerated:', len(S3), 'entries')

import importlib
importlib.reload(step3_data)
S3 = step3_data.S3
print('bad lengths:', [n for n, v in S3.items() if len(v) not in (15, 16)])

# ---- append note sections ----
def tier_short(t):
    if 'Tier 1' in t: return 'Tier 1 - Digital Model (static, no live data)'
    if 'Tier 2' in t: return 'Tier 2 - Digital Shadow (one-way physical to virtual)'
    if 'Tier 3' in t: return 'Tier 3 - Digital Twin (bidirectional, two-way)'
    if 'Tier 4' in t: return 'Tier 4 - Cognitive / Self-improving'
    return 'Unclear'

for n in sorted(ENTRIES):
    slug = S[n][7]
    path = os.path.join(OUT, slug + '.md')
    v = S3[n]
    P, Q, R = v[0], v[1], v[2]
    AG, SRC = v[14], v[15]
    if P == 'Yes' and Q == 'Yes' and R == 'Yes':
        tier, V, W, X, Z, AA, AB, AC, AD, AE, AF = v[3:14]
        sec = ("## Step-3 Deep-Read Coding (Prompt B)\n\n"
               "| P | Q | R | U Tier | V | W | X | Z | AA | AB | AC | AD | AE | AF |\n"
               "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n"
               "| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n\n"
               "**Key evidence (AG):** %s\n\n(full-text source: %s)\n"
               % (P, Q, R, tier_short(tier), V, W, X, Z, AA, AB, AC, AD, AE, AF, AG, SRC))
    else:
        sec = ("## Step-3 Deep-Read Coding (Prompt B)\n\n"
               "**Stage-2 exclusion:** P=%s, Q=%s, R=%s. %s\n\n(full-text source: %s)\n"
               % (P, Q, R, AG, SRC))
    t = open(path, encoding='utf-8').read()
    if '## Step-3 Deep-Read Coding' in t:
        idx = t.rfind('## Step-3')
        t = t[:idx] + sec
    else:
        t = t.rstrip() + '\n\n' + sec
    open(path, 'w', encoding='utf-8').write(t)
    print('note updated:', slug)
