"""Final audit: count blocks, identify schema inconsistencies, list not-checked papers."""
from pathlib import Path
import re

SRC = Path("01_source")

verified_blocks = 0
unverifiable_blocks = 0
not_checked = 0
block_but_not_verified = []  # has ^sec- blocks but zotero_status not verified

for f in sorted(SRC.glob("*.md")):
    t = f.read_text(encoding="utf-8")
    ref_m = re.search(r'ref:\s*"\[(\d+)\]"', t)
    ref = ref_m.group(1) if ref_m else "?"
    ck_m = re.search(r'citekey:\s*"([^"]+)"', t)
    ck = ck_m.group(1) if ck_m else f.stem
    
    has_block = bool(re.search(r'\^sec-', t))
    
    if "zotero_status: verified" in t:
        if has_block: verified_blocks += 1
    elif "zotero_status: unverifiable" in t:
        if has_block: unverifiable_blocks += 1
    else:
        not_checked += 1
        if has_block:
            # Paper has evidence block but zotero_status isn't verified
            vf = "verification_status" in t
            block_but_not_verified.append((ref, ck))

print(f"Verified + blocks:   {verified_blocks}")
print(f"Unverifiable + blocks: {unverifiable_blocks}")
print(f"Not checked:        {not_checked}")
print(f"Has blocks but status not 'verified': {len(block_but_not_verified)}")
for r, ck in block_but_not_verified:
    print(f"  [{r}] {ck}")
print(f"\nTotal notes: {verified_blocks + unverifiable_blocks + not_checked}")
