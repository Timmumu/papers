# -*- coding: utf-8 -*-
import re
d = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round'
t1 = open(d + r'\SLR summary matrix step 1.md', encoding='utf-8').read()
t3 = open(d + r'\SLR summary matrix step 3.md', encoding='utf-8').read()

l1 = t1.splitlines()
l3 = t3.splitlines()
print('step1 total lines:', len(l1), '| data rows:', len([x for x in l1 if re.match(r'^\|\s*\d{4}\s*\|', x)]))
print('step3 total lines:', len(l3), '| data rows:', len([x for x in l3 if re.match(r'^\|\s*\d{4}\s*\|', x)]))
print()
print('--- step1 sample (row 1 and 106) ---')
for x in l1:
    if re.match(r'^\|\s*(3566|3924)\s*\|', x):
        print(x[:260])
print()
print('--- step3 sample (3924) ---')
for x in l3:
    if x.startswith('| 3924 |'):
        print(x[:300])
print()
print('--- step3 missing section ---')
i = next(k for k, x in enumerate(l3) if x.startswith('## Included papers missing'))
print('\n'.join(l3[i-1:i+5]))
print()
# empty cells check
bad1 = [x[:60] for x in l1 if re.match(r'^\|\s*\d{4}\s*\|', x) and ('|  |' in x or '||' in x)]
bad3 = [x[:60] for x in l3 if re.match(r'^\|\s*\d{4}\s*\|', x) and ('|  |' in x or '||' in x)]
print('step1 rows with empty cells:', len(bad1), bad1[:5])
print('step3 rows with empty cells:', len(bad3), bad3[:8])
