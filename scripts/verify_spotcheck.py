import os, re, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from screening_data import S
FT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
txt = open(RIS, encoding='utf-8', errors='replace').read()
recs = re.split(r'\nER  -\s*\n', txt)
meta = {}
n = 0
for r in recs:
    if 'TY  -' not in r:
        continue
    n += 1
    def field(tag):
        m = re.search(rf'^{tag}  - (.*?)(?=^[A-Z0-9]{{2}}  - |\Z)', r, re.M | re.S)
        return ' '.join(m.group(1).split()) if m else ''
    meta[n] = dict(rid=field('ID'), ti=field('TI'))

def norm(s):
    return re.sub(r'[^a-z0-9]', '', s.lower())

targets = ['3572', '3945', '4017', '3863', '3885', '3947', '3661', '3974', '3602', '3968']
for n, m in meta.items():
    if m['rid'] in targets:
        fn = os.path.join(FT, m['rid'] + '_' + S[n][7] + '.txt')
        if not os.path.exists(fn):
            print(m['rid'], 'MISSING FILE', fn)
            continue
        c = open(fn, encoding='utf-8', errors='replace').read().lower()
        cn = norm(c)
        tn = norm(m['ti'])
        print('[%s] %s' % (m['rid'], S[n][7]))
        print('  title_len=%d' % len(tn))
        print('  fulltitle_in_text=%s' % (len(tn) >= 40 and tn in cn))
        print('  title_in_first4000=%s' % (len(tn) >= 40 and tn in cn[:4000]))
