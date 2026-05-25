"""Deep audit: which verified papers have evidence blocks vs just status=verified."""
from pathlib import Path
import re

SRC = Path("01_source")

has_blocks = []   # verified + has ^sec- block IDs
no_blocks = []    # verified but no evidence blocks
unverifiable_no_blocks = []  # unverifiable without sec-abstract

for f in sorted(SRC.glob("*.md")):
    t = f.read_text(encoding="utf-8")
    ref_m = re.search(r'ref:\s*"\[(\d+)\]"', t)
    ref = ref_m.group(1) if ref_m else "?"
    ck_m = re.search(r'citekey:\s*"([^"]+)"', t)
    ck = ck_m.group(1) if ck_m else f.stem
    
    has_block_ids = bool(re.search(r'\^sec-', t))  # evidence blocks exist
    
    if "zotero_status: verified" in t:
        if has_block_ids:
            has_blocks.append((ref, ck))
        else:
            no_blocks.append((ref, ck))
    elif "zotero_status: unverifiable" in t:
        if not has_block_ids:
            unverifiable_no_blocks.append((ref, ck))

print(f"Verified WITH evidence blocks:  {len(has_blocks)}")
for r, ck in has_blocks: print(f"  [{r}] {ck}")

print(f"\nVerified WITHOUT evidence blocks: {len(no_blocks)} ← NEEDS ATTENTION")
for r, ck in no_blocks: print(f"  [{r}] {ck}")

print(f"\nUnverifiable WITHOUT sec-abstract: {len(unverifiable_no_blocks)} ← NEEDS ATTENTION")
for r, ck in unverifiable_no_blocks[:20]: print(f"  [{r}] {ck}")
if len(unverifiable_no_blocks) > 20: print(f"  ... and {len(unverifiable_no_blocks)-20} more")
