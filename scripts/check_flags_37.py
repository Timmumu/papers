"""Check citekey mismatches and missing notes."""
import re
from pathlib import Path

# Flag 7: citekey mismatches
checks = {
    'Pereira2025': 'Martinez-Rojas 2025',
    'Kulinan2024': 'Liu 2023',
    'Kim2025': 'Chen 2025',
    'Wang2026': 'Omrany 2026',
    'Fu2026': 'Lu 2025',
}
print("=== Flag 7: Citekey mismatches ===")
for ck, expected_author in checks.items():
    fp = Path(f'01_source/{ck}.md')
    if fp.exists():
        t = fp.read_text(encoding='utf-8')
        ref_m = re.search(r'ref:\s*"\[([0-9]+)\]"', t)
        auth_m = re.search(r'authors:\s*"([^"]+)"', t)
        doi_m = re.search(r'doi:\s*"?(10\.[^"\s]+)"?', t)
        print(f'{ck}.md: ref=[{ref_m.group(1) if ref_m else "?"}]')
        print(f'  authors: {auth_m.group(1)[:100] if auth_m else "?"}')
        print(f'  expected: {expected_author}')
        print(f'  DOI: {doi_m.group(1) if doi_m else "?"}')
        print()

# Flag 3: Missing notes
print("=== Flag 3: Missing backing notes ===")
for ck in ['Kahneman2021', 'Lee2006']:
    fp = Path(f'01_source/{ck}.md')
    print(f'{ck}.md: exists={fp.exists()}')
    if fp.exists():
        t = fp.read_text(encoding='utf-8')
        ref_m = re.search(r'ref:\s*"\[([0-9]+)\]"', t)
        print(f'  ref=[{ref_m.group(1) if ref_m else "?"}]')
