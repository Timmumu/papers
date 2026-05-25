"""Batch-add [[citekey]] wikilinks after all [N] citations in LR_GPT.md."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LR = ROOT / "MD" / "LR_GPT.md"
SRC = ROOT / "01_source"

# Build [N] -> citekey map from 01_source frontmatter
ref_map = {}
for f in SRC.glob("*.md"):
    text = f.read_text(encoding="utf-8")
    m = re.search(r'ref:\s*"\[(\d+)\]"', text)
    if not m: continue
    ref = m.group(1)
    ck_m = re.search(r'citekey:\s*"([^"]+)"', text)
    citekey = ck_m.group(1) if ck_m else f.stem
    ref_map[ref] = citekey

print(f"Loaded {len(ref_map)} citekey mappings")

text = LR.read_text(encoding="utf-8")
# Split at References section to protect it
parts = text.split("## 8. References", 1)
if len(parts) != 2:
    print("ERROR: Could not split at References section")
    exit(1)
body, refs = parts

# Find all [N] in body (not already followed by [[)
def replace_cb(m):
    num = m.group(1)
    if num not in ref_map:
        return m.group(0)
    # Check if already has wikilink ([[ or thin-space [[)
    rest = body[m.end():m.end()+30]
    if rest.startswith(" [[") or rest.startswith("\u202f[[") or rest.startswith("]\n[["):
        return m.group(0)  # already linked
    return f"[{num}] [[{ref_map[num]}]]"

# Preview mode: just count, don't write
import sys
dry_run = "--dry" in sys.argv

body_new = re.sub(r"\[(\d+)\](?!\s*\[\[)", replace_cb, body)
added = len(re.findall(r"\[\[\w", body_new)) - len(re.findall(r"\[\[\w", body))
skipped = 0  # already-linked ones we protected

if dry_run:
    print(f"DRY RUN: Would add ~{added} wikilinks. No file changes.")
    # Show first few changes
    for m in re.finditer(r"\[(\d+)\]\s*\[\[(\w[^\]]+)\]\]", body_new):
        if m.group(1) in ref_map:
            num, ck = m.group(1), m.group(2)
            idx = m.start()
            ctx = body_new[max(0,idx-30):idx+40].replace('\n',' ')
            print(f"  [{num}] [[{ck}]]  ...{ctx}...")
            break
else:
    new_text = body_new + "## 8. References" + refs
    LR.write_text(new_text, encoding="utf-8")
    print(f"Added ~{added} wikilinks. File updated.")
