import re, sys

src = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\429 papers.txt'
N_START = int(sys.argv[1]) if len(sys.argv) > 1 else 1
N_END = int(sys.argv[2]) if len(sys.argv) > 2 else 100
out_path = rf'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\batch{N_START}-{N_END}.txt'

txt = open(src, encoding='utf-8', errors='replace').read()
recs = re.split(r'\nER  -\s*\n', txt)
out = []
n = 0
for r in recs:
    if 'TY  -' not in r:
        continue
    n += 1
    if n < N_START:
        continue
    if n > N_END:
        break

    def field(tag):
        m = re.search(rf'^{tag}  - (.*?)(?=^[A-Z0-9]{{2}}  - |\Z)', r, re.M | re.S)
        return ' '.join(m.group(1).split()) if m else ''

    rid = field('ID'); ti = field('TI'); ab = field('AB'); db = field('DB')
    aus = re.findall(r'^AU  - (.*)$', r, re.M)
    py = field('PY'); do = field('DO'); t2 = field('T2')
    srcdb = db if db else ('Web of Science' if 'WOS:' in r else 'Lens.org')
    au_str = '; '.join(aus[:4])
    out.append(f'### {n}. ID {rid} | {srcdb}\nTI: {ti}\nAU: {au_str}\nPY: {py} | T2: {t2} | DO: {do}\nAB: {ab}\n')

open(out_path, 'w', encoding='utf-8').write('\n'.join(out))
print('parsed records', N_START, '-', min(n, N_END), '->', out_path)
