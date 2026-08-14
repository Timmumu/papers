"""Verify each extracted full text matches its expected paper title."""
import os, re, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from screening_data import S

RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
FT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'

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
    s = s.lower()
    s = re.sub(r'[^a-z0-9 ]', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()

STOP = {'digital','twin','twins','construction','based','using','model','models','framework','system','review','study','analysis','applications','application','management','monitoring','building','buildings','with','for','and','the','a','an','of','in','on','to','method','methods','approach','toward','towards','via','from','its','their','new','real','time','evaluation','research','an','into','as','is','are','be'}

def distinct_words(ti):
    words = norm(ti).split()
    return [w for w in words if len(w) > 4 and w not in STOP]

checked, mismatched = [], []
for f in sorted(os.listdir(FT)):
    if not f.endswith('.txt'):
        continue
    slug = f[:-4]
    if '_' in slug:
        slug = slug.split('_', 1)[1]
    idx = None
    for n in range(1, 430):
        if S[n][7] == slug:
            idx = n
            break
    if idx is None:
        continue
    exp_ti = meta[idx]['ti']
    try:
        content = open(os.path.join(FT, f), encoding='utf-8', errors='replace').read()
    except Exception:
        continue
    ncontent = norm(content)
    distinct = distinct_words(exp_ti)
    if not distinct:
        checked.append((idx, f, 'OK'))
        continue
    hits = sum(1 for w in distinct if w in ncontent)
    ratio = hits / len(distinct)
    if ratio >= 0.6:
        checked.append((idx, f, 'OK' if ratio >= 0.8 else 'FUZZY'))
    else:
        mismatched.append((idx, f, exp_ti[:70], ratio))

print(f'checked {len(checked)} texts; MISMATCHED {len(mismatched)}:')
for idx, f, eti, got in mismatched:
    print(f'#{idx} {f}\n   EXPECT: {eti}\n   word-ratio: {got:.2f}')
for idx, f, st in checked:
    if st == 'FUZZY':
        print(f'FUZZY #{idx} {f}')
