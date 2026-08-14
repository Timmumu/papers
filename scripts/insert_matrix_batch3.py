"""Insert the 25 newly coded Step-3 rows into the matrix Step-3 table.
Reads S3 + screening_data, formats rows to match existing table style.
"""
import sys, re
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from step3_data import S3
from screening_data import S

RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
MAT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\SLR summary matrix.md'

# parse RIS for rid (ID field)
txt = open(RIS, encoding='utf-8', errors='replace').read()
recs = re.split(r'\nER  -\s*\n', txt)
rid = {}
n = 0
for r in recs:
    if 'TY  -' not in r:
        continue
    n += 1
    m = re.search(r'^ID  - (.*?)(?=^[A-Z0-9]{2}  - |\Z)', r, re.M | re.S)
    rid[n] = m.group(1).strip() if m else str(n)

NEW = [14,20,66,86,92,100,115,165,178,219,253,262,265,271,299,309,315,331,334,354,376,389,402,412,423]

def tier_short(t):
    if 'Tier 1' in t: return 'Tier 1 - Digital Model (static, no live data)'
    if 'Tier 2' in t: return 'Tier 2 - Digital Shadow (one-way physical to virtual)'
    if 'Tier 3' in t: return 'Tier 3 - Digital Twin (bidirectional, two-way)'
    if 'Tier 4' in t: return 'Tier 4 - Cognitive / Self-improving'
    return 'Unclear'

rows = []
for n in NEW:
    v = S3[n]
    P,Q,R,tier,V,W,X,Z,AA,AB,AC,AD,AE,AF,AG = v
    rows.append(f'| {rid[n]} | {P} | {Q} | {R} | {tier_short(tier)} | {V} | {W} | {X} | {Z} | {AA} | {AB} | {AC} | {AD} | {AE} | {AF} | {AG} |')

block = '\n'.join(rows)
mat = open(MAT, encoding='utf-8').read()

# find end of the Step-3 table (last data row before a new heading or EOF)
idx = mat.find('| 3906 |')  # last existing row
if idx < 0:
    print('anchor not found')
    sys.exit(1)
# find end of that line
end = mat.find('\n', idx)
insert_at = end + 1
new_mat = mat[:insert_at] + '\n' + block + '\n' + mat[insert_at:]
open(MAT, 'w', encoding='utf-8').write(new_mat)
print('inserted', len(rows), 'rows after existing Step-3 rows')
print('sample first row:', rows[0][:120])
