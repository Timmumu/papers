"""Phase 2: Diagnose integrity flags."""
import re
from pathlib import Path

# Flag 2: Ref [63] double-claim
print("=== Flag 2: Ref [63] double-claim ===")
for md in Path('01_source').glob('*.md'):
    t = md.read_text(encoding='utf-8')
    ref_m = re.search(r'ref:\s*"\[63\]"', t)
    if ref_m:
        print(f'  [63] claimed by: {md.name}')
for md in Path('02_removed').glob('*.md'):
    t = md.read_text(encoding='utf-8')
    ref_m = re.search(r'ref:\s*"\[63\]"', t)
    if ref_m:
        print(f'  [63] claimed by (02_removed): {md.name}')
print('  → No [63] claimants in 01_source = flag resolved')

# Flag 6: Removed-but-cited
print("\n=== Flag 6: Removed-but-cited ===")
for md in Path('02_removed').glob('*Charters*'):
    print(f'  [27] Charters in 02_removed: {md.name}')
for md in Path('02_removed').glob('*Saltelli*'):
    print(f'  [47] Saltelli in 02_removed: {md.name}')
# Check if Charters has a note in 01_source
if Path('01_source/Charters2007.md').exists():
    print('  [27] Charters2007.md EXISTS in 01_source')
else:
    print('  [27] Charters2007.md MISSING from 01_source')

# Flag 8: Hosamo1988 filename
print("\n=== Flag 8: Hosamo1988 ===")
hosamo = Path('01_source/Hosamo1988.md')
if hosamo.exists():
    t = hosamo.read_text(encoding='utf-8')
    ck = re.search(r'citekey:\s*"([^"]+)"', t)
    yr = re.search(r'year:\s*(\d+)', t)
    doi_m = re.search(r'doi:\s*"?(10\.[^"\s]+)"?', t)
    print(f'  citekey={ck.group(1) if ck else "?"}')
    print(f'  year={yr.group(1) if yr else "?"}')
    print(f'  doi={doi_m.group(1) if doi_m else "?"}')

# Flag 9: AlOmari2026 mojibake
print("\n=== Flag 9: AlOmari2026 mojibake ===")
amo = Path('01_source/AlOmari2026.md')
if amo.exists():
    t = amo.read_text(encoding='utf-8')
    # Check for mojibake - look for replacement chars or CJK encoding artifacts
    has_mojibake = False
    for i, ch in enumerate(t[:1000]):
        if ord(ch) in [0xFFFD, 0xBFBD] or (0xE900 <= ord(ch) <= 0xE999):
            has_mojibake = True
            break
    if '鈥' in t or has_mojibake:
        print('  ⚠ CONTAINS MOJIBAKE')
        # Show authors line
        auth_m = re.search(r'authors:\s*"([^"]*)"', t)
        if auth_m:
            print(f'  authors: {auth_m.group(1)[:200]}')
    else:
        print('  Appears clean')

# Flag 4: [91] Tao2019b
print("\n=== Flag 4: [91] Tao2019b ===")
t2019b = Path('01_source/Tao2019b.md')
t2019 = Path('01_source/Tao2019.md')
print(f'  Tao2019b.md exists: {t2019b.exists()}')
print(f'  Tao2019.md exists: {t2019.exists()}')
if t2019b.exists():
    tb = t2019b.read_text(encoding='utf-8')
    doi_b = re.search(r'doi:\s*"?(10\.[^"\s]+)"?', tb)
    print(f'  Tao2019b DOI: {doi_b.group(1) if doi_b else "?"}')
    ref_b = re.search(r'ref:\s*"\[(\d+)\]"', tb)
    print(f'  Tao2019b ref: [{ref_b.group(1) if ref_b else "?"}]')
if t2019.exists():
    ta = t2019.read_text(encoding='utf-8')
    doi_a = re.search(r'doi:\s*"?(10\.[^"\s]+)"?', ta)
    print(f'  Tao2019 DOI: {doi_a.group(1) if doi_a else "?"}')
    ref_a = re.search(r'ref:\s*"\[(\d+)\]"', ta)
    print(f'  Tao2019 ref: [{ref_a.group(1) if ref_a else "?"}]')

# Flag 5: Check duplicate pairs
print("\n=== Flag 5: Duplicate note pairs ===")
dup_pairs = [
    ('Degani2024', 'Spinner2024'),
    ('Zhang2021', 'Pan&Zhang2021'),
    ('Rasheed1980', 'Rasheed2020'),
    ('Glaessgen2012', 'Stargel2012'),
    ('Grieves2026', 'Vickers2017'),
    ('Liu&Meng2021', 'Liu2021'),
    ('Ruppert2018', 'Ruppert2020'),
]
for a, b in dup_pairs:
    a_exists = Path(f'01_source/{a}.md').exists()
    b_exists = Path(f'01_source/{b}.md').exists()
    if a_exists and b_exists:
        print(f'  ⚠ BOTH exist: {a}.md AND {b}.md → needs merge')
    elif a_exists:
        print(f'  ✓ Only {a}.md exists (OK)')
    elif b_exists:
        print(f'  ✓ Only {b}.md exists (OK)')
    else:
        print(f'  ✗ NEITHER exists: {a}.md, {b}.md')
