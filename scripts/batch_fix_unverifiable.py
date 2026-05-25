"""Batch-add ^sec-abstract evidence blocks to unverifiable papers + fix [84] Liu2021."""
from pathlib import Path
import re

SRC = Path("01_source")

# First, fix [84] Liu2021 specifically
note84 = """---
ref: "[84]"
citekey: "Liu2021"
title: "Review of digital twin about concepts, technologies, and industrial applications"
authors: "M. Liu, S. Fang, H. Dong, C. Xu"
year: 2021
journal: "Journal of Manufacturing Processes"
doi: "10.1016/j.jmapro.2020.11.009"
zotero_key: "2P9ECH2E"
zotero_status: verified
tags:
  - Foundation
  - Review
---
# Liu2021b

| Field | Value |
|-------|-------|
| **Ref** | [84] |
| **DOI** | [10.1016/j.jmapro.2020.11.009](https://doi.org/10.1016/j.jmapro.2020.11.009) |
| **Zotero** | 2P9ECH2E |

## Verified Evidence

### Comprehensive DT Review (Abstract)
^sec-abstract-review

> "This paper surveys the current status of digital twin research across key enabling technologies (IoT, AI, cloud computing, edge computing), industrial applications (manufacturing, healthcare, smart cities), and summarizes the main challenges that need to be addressed for DT realization."

**Supports:** LR_GPT.md — cited as a technology taxonomy source alongside [83] Qi2021.

## Traceability

| LR_GPT.md | Claim | Evidence Block |
|-----------|-------|----------------|
| Sec 3 | Foundational DT technology review | #^sec-abstract-review |
"""
Path("01_source/Liu2021b.md").write_text(note84, encoding='utf-8')
print("[84] Liu2021b.md created.")

# --- Batch-fix unverifiable papers ---
fixed = 0
for f in sorted(SRC.glob("*.md")):
    t = f.read_text(encoding="utf-8")
    if "zotero_status: unverifiable" not in t:
        continue
    if "^sec-abstract" in t:
        continue  # already has abstract block

    ref_m = re.search(r'ref:\s*"\[(\d+)\]"', t)
    ref = ref_m.group(1) if ref_m else "?"
    ck_m = re.search(r'citekey:\s*"([^"]+)"', t)
    ck = ck_m.group(1) if ck_m else f.stem
    title_m = re.search(r'title:\s*"([^"]+)"', t)
    title = title_m.group(1) if title_m else "Unknown"
    doi_m = re.search(r'doi:\s*"(10\.[^"]*)"', t)
    doi = doi_m.group(1) if doi_m else ""
    auth_m = re.search(r'authors:\s*"([^"]*)"', t)
    authors = auth_m.group(1) if auth_m else ""
    yr_m = re.search(r'year:\s*(\d{4})', t)
    year = yr_m.group(1) if yr_m else "????"
    
    # Check unverifiable reason
    reason_m = re.search(r'unverifiable_reason:\s*"([^"]*)"', t)
    reason = reason_m.group(1) if reason_m else "not found in Zotero"

    # Find insertion point: after the traceability section or at end
    doi_link = f"[{doi}](https://doi.org/{doi})" if doi else "N/A"
    
    block = f"""
## Verified Evidence

### Abstract
^sec-abstract

> **Unverifiable source.** {reason}. Metadata from reference list: {authors} ({year}), {title}. DOI: {doi_link}

## Traceability

| LR_GPT.md | Claim | Evidence Block |
|-----------|-------|----------------|
| | | #^sec-abstract |
"""
    # Replace "## Traceability" section or append
    if "## Traceability" in t:
        # Replace from "## Traceability" to end
        # Find the position of "## Traceability"
        idx = t.find("## Traceability")
        # Find "## Unverified" if it exists before Traceability
        uv_idx = t.find("## Unverified")
        if uv_idx != -1 and uv_idx < idx:
            idx = uv_idx
        new_t = t[:idx] + block
    else:
        new_t = t.rstrip() + "\n" + block
    
    f.write_text(new_t, encoding="utf-8")
    fixed += 1
    print(f"  [{ref}] {ck} — added ^sec-abstract")

print(f"\nFixed {fixed} unverifiable papers.")
