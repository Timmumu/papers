"""Check which citekeys in duplicate pairs are referenced in LR.md."""
import re
from pathlib import Path

lr = Path('LR 2round/LR.md').read_text(encoding='utf-8')

# Find all wikilinks [[citekey...]]
wikilinks = set()
for m in re.finditer(r'\[\[(\w[^\]|#]*)', lr):
    wikilinks.add(m.group(1))

# Duplicate pairs with their keep/remove from size-based analysis
pairs = {
    'Degani2024': 'Spinner2024',
    'Zhang2021': 'Pan&Zhang2021',  
    'Rasheed1980': 'Rasheed2020',
    'Glaessgen2012': 'Stargel2012',
    'Grieves2026': 'Vickers2017',
    'Liu&Meng2021': 'Liu2021',
    'Ruppert2018': 'Ruppert2020',
}

for remove_candidate, keep_candidate in pairs.items():
    r_in_lr = remove_candidate in wikilinks
    k_in_lr = keep_candidate in wikilinks
    print(f'{remove_candidate}: in LR.md={r_in_lr} | {keep_candidate}: in LR.md={k_in_lr}')
    
    if r_in_lr and not k_in_lr:
        print(f'  ⚠ LR.md links to {remove_candidate} but plan moves it! KEEP {remove_candidate} instead.')
    elif not r_in_lr and k_in_lr:
        print(f'  ✓ LR.md links to {keep_candidate} — safe to move {remove_candidate}')
    elif r_in_lr and k_in_lr:
        print(f'  ⚠ BOTH referenced — need to choose one and update LR.md wikilinks')
    else:
        print(f'  Neither referenced — either choice OK')
    print()
