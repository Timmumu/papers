"""Write a resolve report: for each included paper, best matching text + ratio."""
import os, re, sys
sys.path.insert(0, r'h:\phd\6.pjt\LR1\papers\scripts')
from screening_data import S

RIS = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
FT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
OUT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\resolve_report.txt'

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

STOP = {'digital','twin','twins','construction','based','using','model','models','framework','system','review','study','analysis','applications','application','management','monitoring','building','buildings','with','for','and','the','a','an','of','in','on','to','method','methods','approach','toward','towards','via','from','its','their','new','real','time','evaluation','research','an','into','as','is','are','be','paper','article'}

def distinct(ti):
    return [w for w in norm(ti).split() if len(w) > 4 and w not in STOP]

texts = {}
for f in os.listdir(FT):
    if f.endswith('.txt'):
        try:
            texts[f] = norm(open(os.path.join(FT, f), encoding='utf-8', errors='replace').read())
        except Exception:
            pass

lines = []
for n in range(1, 430):
    if S[n][5] != 'Include':
        continue
    ti = meta[n]['ti']
    d = distinct(ti)
    scored = []
    for f, nc in texts.items():
        hits = sum(1 for w in d if w in nc)
        r = hits / len(d) if d else 0
        scored.append((r, f))
    scored.sort(reverse=True)
    best_r, best_f = scored[0]
    second = scored[1] if len(scored) > 1 else (0, '')
    lines.append(f'#{n} [{meta[n]["rid"]}] {S[n][7]}')
    lines.append(f'   BEST: {best_f}  ratio={best_r:.2f}  2nd: {second[1]} {second[0]:.2f}')
    lines.append(f'   EXP: {ti[:75]}')

open(OUT, 'w', encoding='utf-8').write('\n'.join(lines))
print('wrote', OUT, 'with', sum(1 for l in lines if l.startswith('#')), 'papers')
