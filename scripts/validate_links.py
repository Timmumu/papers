"""Validate: every [[citekey#^block-id]] in LR_GPT.md points to an existing block in 01_source."""
from pathlib import Path
import re

LR = Path("MD/LR_GPT.md").read_text(encoding="utf-8")
SRC = Path("01_source")

# Build block index: citekey -> set of block IDs
blocks = {}
for f in SRC.glob("*.md"):
    ck = f.stem
    t = f.read_text(encoding="utf-8")
    # Find all ^sec-xxx block IDs in the file
    found = set(re.findall(r'(\^sec-[a-zA-Z0-9_-]+)', t))
    if found:
        blocks[ck] = found
        # Also index by citekey from frontmatter
        ck_m = re.search(r'citekey:\s*"([^"]+)"', t)
        if ck_m:
            blocks[ck_m.group(1)] = found

# Find all wikilinks with block IDs in LR_GPT.md
links = re.findall(r'\[\[(\w[^\]|#]*)#(\^[^\]]+)\]\]', LR)

broken = []
ok = 0
for note_name, block_id in links:
    if note_name in blocks:
        if block_id in blocks[note_name]:
            ok += 1
        else:
            broken.append((note_name, block_id, list(blocks[note_name])[:3]))
    else:
        broken.append((note_name, block_id, "NOTE NOT FOUND"))

print(f"OK links: {ok}")
print(f"Broken links: {len(broken)}")
for note, bid, avail in broken[:20]:
    print(f"  [[{note}#{bid}]] — available: {avail}")
if len(broken) > 20:
    print(f"  ... and {len(broken)-20} more")

# Also count bare wikilinks (no block ID)
bare = re.findall(r'\[\[(\w[^\]|#]+)\]\](?!#)', LR)
print(f"\nBare wikilinks (no block ID): {len(bare)}")
