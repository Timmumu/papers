"""Analyze duplicate pairs to determine keep vs remove."""
import re
from pathlib import Path

pairs = [
    ('Degani2024', 'Spinner2024', 'ULJGBQZ6'),
    ('Zhang2021', 'Pan&Zhang2021', 'YGJSXUXV'),
    ('Rasheed1980', 'Rasheed2020', 'MKZ3HU7D'),
    ('Glaessgen2012', 'Stargel2012', '8B7R5BZU'),
    ('Grieves2026', 'Vickers2017', '83PUTURG'),
    ('Liu&Meng2021', 'Liu2021', 'CDL7QW8N'),
    ('Ruppert2018', 'Ruppert2020', 'IJUPSPJB'),
]
for a, b, key in pairs:
    fa = Path(f'01_source/{a}.md')
    fb = Path(f'01_source/{b}.md')
    if fa.exists() and fb.exists():
        sa = fa.stat().st_size
        sb = fb.stat().st_size
        ta = fa.read_text(encoding='utf-8')
        tb = fb.read_text(encoding='utf-8')
        ba = bool(re.search(r'\^sec-', ta))
        bb = bool(re.search(r'\^sec-', tb))
        ra = re.search(r'ref:\s*"\[([0-9]+)\]"', ta)
        rb = re.search(r'ref:\s*"\[([0-9]+)\]"', tb)
        ref_a = ra.group(1) if ra else '?'
        ref_b = rb.group(1) if rb else '?'
        # Check zotero_status
        zs_a = re.search(r'zotero_status:\s*(\S+)', ta)
        zs_b = re.search(r'zotero_status:\s*(\S+)', tb)
        
        keeper = a if sa >= sb else b
        remove = b if sa >= sb else a
        print(f'{a}({sa}B, ref=[{ref_a}], blocks={ba}, status={zs_a.group(1) if zs_a else "?"})')
        print(f'  vs {b}({sb}B, ref=[{ref_b}], blocks={bb}, status={zs_b.group(1) if zs_b else "?"})')
        print(f'  => KEEP: {keeper}, MOVE to 02_removed: {remove}')
        print()
