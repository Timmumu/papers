"""EndNote Verification Pipeline: upgrade zotero_status for all 01_source notes.
Usage:
  python scripts/verify_endnote.py --dry-run     (report only)
  python scripts/verify_endnote.py --upgrade      (apply upgrades)
  python scripts/verify_endnote.py --upgrade --limit 50
"""
import sqlite3, re, sys
from pathlib import Path
from collections import Counter

ENL = r"H:\phd\paper\Endnote\My EndNote Library.enl.backup"
NOTES = Path("01_source")

dry_run = "--dry-run" in sys.argv
do_upgrade = "--upgrade" in sys.argv
limit = None
for i, a in enumerate(sys.argv):
    if a == "--limit" and i+1 < len(sys.argv):
        limit = int(sys.argv[i+1])

# 1. Scan notes
print("[1/4] Scanning 01_source...")
notes = {}
for md in sorted(NOTES.glob("*.md")):
    t = md.read_text(encoding="utf-8")
    doi_m = re.search(r'doi:\s*"?(10\.[^"\s\n]+)"?', t)
    doi = doi_m.group(1).strip().lower() if doi_m else ""
    zs_m = re.search(r'zotero_status:\s*(\S+)', t)
    zs = zs_m.group(1) if zs_m else "not-checked"
    ck_m = re.search(r'citekey:\s*"([^"]+)"', t)
    ck = ck_m.group(1) if ck_m else md.stem
    notes[doi if doi else f"NO_DOI_{md.stem}"] = {"file": md, "citekey": ck, "status": zs}

before_ctr = Counter(n["status"] for n in notes.values())
print(f"  Total: {len(notes)}")
print(f"  Before: {dict(before_ctr)}")

# 2. Load EndNote
print("[2/4] Loading EndNote...")
conn = sqlite3.connect(ENL)
c = conn.cursor()
c.execute("""SELECT r.electronic_resource_number, r.abstract, f.file_path
    FROM refs r LEFT JOIN file_res f ON r.id = f.refs_id WHERE r.trash_state = 0""")
enl = {}
for doi_raw, abstract, pdf_raw in c.fetchall():
    doi = (doi_raw or "").strip().lower()
    pdf = (pdf_raw or "").replace("internal-pdf://", "").strip()
    if doi:
        enl[doi] = {"abstract": abstract or "", "pdf": pdf if pdf else None}
conn.close()

pdf_ct = sum(1 for e in enl.values() if e["pdf"])
abs_ct = sum(1 for e in enl.values() if e["abstract"])
print(f"  EndNote refs: {len(enl)} (PDF={pdf_ct}, abstract={abs_ct})")

# 3. Match and classify
print("[3/4] Matching...")
pdf_match, abs_match, no_match = [], [], []
for key, nd in notes.items():
    if key.startswith("NO_DOI_"):
        no_match.append(nd)
        continue
    e = enl.get(key)
    if e and e["pdf"]:
        pdf_match.append({**nd, "enl": e})
    elif e and e["abstract"]:
        abs_match.append({**nd, "enl": e})
    else:
        no_match.append(nd)

print(f"  PDF match: {len(pdf_match)}, Abstract-only: {len(abs_match)}, No match: {len(no_match)}")

# 4. Plan upgrades
print("[4/4] Upgrade plan:")
upgrades = []
# PDF matches -> verified (except already verified)
for m in pdf_match:
    old = m["status"]
    if old != "verified":
        upgrades.append((m["file"], old, "verified", "EndNote PDF"))
# Abstract-only matches -> abstract-grounded (upgrade from title-only/unsorted/not-checked)
for m in abs_match:
    old = m["status"]
    if old in ("title-only", "unsorted", "not-checked", "partial", "fulltext-oa"):
        upgrades.append((m["file"], old, "abstract-grounded", "EndNote abstract"))
# No match, title-only -> stays title-only (flagged)
for m in no_match:
    if m["status"] == "title-only":
        upgrades.append((m["file"], "title-only", "title-only", "no EndNote match -- manual needed"))
    elif m["status"] == "unsorted":
        upgrades.append((m["file"], "unsorted", "not-checked", "no EndNote match -- review needed"))

ctr = Counter(f"{o}->{n}" for _, o, n, _ in upgrades)
print(f"  Actions: {dict(ctr)}")

if dry_run:
    print("\n  DRY RUN -- no changes. Use --upgrade to apply.")
    for f, o, n, r in upgrades[:25]:
        print(f"    {f.name}: {o} -> {n}  ({r})")
    if len(upgrades) > 25:
        print(f"    ... and {len(upgrades)-25} more")
    sys.exit(0)

if not do_upgrade:
    print("\n  Run with --upgrade to apply.")
    sys.exit(0)

# 5. Apply
print(f"\n  Applying {len(upgrades)} upgrades...")
applied = 0
for f, old, new, reason in upgrades:
    if limit and applied >= limit:
        break
    t = f.read_text(encoding="utf-8")
    nt = re.sub(r'zotero_status:\s*\S+', f'zotero_status: {new}', t, count=1)
    if nt != t:
        f.write_text(nt, encoding="utf-8")
        applied += 1
        if applied <= 40:
            print(f"    {f.name}: {old} -> {new}")

print(f"\n  Applied: {applied} upgrades")

# Final stats
notes2 = {}
for md in sorted(NOTES.glob("*.md")):
    t = md.read_text(encoding="utf-8")
    zs_m = re.search(r'zotero_status:\s*(\S+)', t)
    zs = zs_m.group(1) if zs_m else "not-checked"
    notes2[md.stem] = zs
after_ctr = Counter(notes2.values())
print(f"  After: {dict(after_ctr)}")
