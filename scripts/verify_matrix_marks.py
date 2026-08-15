# -*- coding: utf-8 -*-
import re
t = open(r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\SLR summary matrix.md', encoding='utf-8').read()
step3 = t[t.find('## Step 3'):]
print('Endnote marks:', step3.count('[Full-text source: Endnote]'))
print('arXiv marks:', step3.count('[Full-text source: arXiv OA preprint]'))
print('MDPI marks:', step3.count('[Full-text source: MDPI Buildings'))
rows = [l for l in step3.splitlines() if re.match(r'^\| \d{4} \|', l)]
nofull = sum(1 for l in rows if '[Full-text source:' not in l)
print('rows:', len(rows), '| rows WITHOUT source mark:', nofull)
