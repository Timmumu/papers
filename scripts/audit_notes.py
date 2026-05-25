"""Audit 01_source notes: count verified/unverifiable/not_checked, list refs."""
from pathlib import Path
import re

SRC = Path("01_source")
verified = []
unverifiable = []
not_checked = []
needs_zotero = []  # has DOI but no zotero_key

for f in sorted(SRC.glob("*.md")):
    t = f.read_text(encoding="utf-8")
    ref_m = re.search(r'ref:\s*"\[(\d+)\]"', t)
    ref = ref_m.group(1) if ref_m else "?"
    
    ck_m = re.search(r'citekey:\s*"([^"]+)"', t)
    ck = ck_m.group(1) if ck_m else f.stem
    
    doi_m = re.search(r'doi:\s*"(10\.[^"]+)"', t)
    doi = doi_m.group(1) if doi_m else ""
    
    zk_m = re.search(r'zotero_key:\s*"([^"]*)"', t)
    zk = zk_m.group(1) if zk_m else ""
    
    if "zotero_status: verified" in t:
        verified.append((ref, ck, zk))
    elif "zotero_status: unverifiable" in t:
        unverifiable.append((ref, ck))
    else:
        not_checked.append((ref, ck))
        if doi and not zk:
            needs_zotero.append((ref, ck, doi))

print(f"=== Audit Summary ===")
print(f"Verified:     {len(verified)}")
for r, ck, zk in verified[:12]: print(f"  [{r}] {ck} (zk={zk})")
if len(verified) > 12: print(f"  ... and {len(verified)-12} more")

print(f"\nUnverifiable: {len(unverifiable)}")
for r, ck in unverifiable[:10]: print(f"  [{r}] {ck}")
if len(unverifiable) > 10: print(f"  ... and {len(unverifiable)-10} more")

print(f"\nNot checked:  {len(not_checked)}")
print(f"  → With DOI but no Zotero key: {len(needs_zotero)}")
for r, ck, doi in needs_zotero[:15]: print(f"  [{r}] {ck}  doi:{doi}")
if len(needs_zotero) > 15: print(f"  ... and {len(needs_zotero)-15} more")

print(f"\nTotal notes: {len(verified)+len(unverifiable)+len(not_checked)}")
