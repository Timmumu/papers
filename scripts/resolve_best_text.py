"""For each included paper, find the BEST matching full text across all .txt files
by content (title-word overlap), NOT by filename. Outputs a resolve report.
"""
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

STOP = {'digital','twin','twins','construction','based','using','model','models','framework','system','review','study','analysis','applications','application','management','monitoring','building','buildings','with','for','and','the','a','an','of','in','on','to','method','methods','approach','toward','towards','via','from','its','their','new','real','time','evaluation','research','an','into','as','is','are','be','paper','article','using','for','an'}

def distinct(ti):
    return [w for w in norm(ti).split() if len(w) > 4 and w not in STOP]

# load all texts once
texts = {}
for f in os.listdir(FT):
    if f.endswith('.txt'):
        try:
            texts[f] = open(os.path.join(FT, f), encoding='utf-8', errors='replace').read()
        except Exception:
            pass

included = [n for n in range(1, 430) if S[n][5] == 'Include']
resolved, unresolved = [], []
for n in included:
    ti = meta[n]['ti']
    d = distinct(ti)
    best_f, best_ratio = None, 0.0
    for f, c in texts.items():
        nc = norm(c)
        hits = sum(1 for w in d if w in nc)
        ratio = hits / len(d) if d else 0
        if ratio > best_ratio:
            best_ratio, best_f = ratio, f
    if best_f and best_ratio >= 0.6:
        resolved.append((n, meta[n]['rid'], S[n][7], best_f, round(best_ratio, 2)))
    else:
        unresolved.append((n, meta[n]['rid'], S[n][7], meta[n]['ti'][:70]))

print(f'RESOLVED: {len(resolved)} / {len(included)}')
print('\n--- UNRESOLVED (no full text with >=60% title match) ---')
for n, rid, slug, ti in unresolved:
    print(f'#{n} [{rid}] {slug} | {ti}')
