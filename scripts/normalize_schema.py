"""Add zotero_status: verified to notes that have evidence blocks but use different field name."""
from pathlib import Path
import re

SRC = Path("01_source")
fixed = 0

for f in sorted(SRC.glob("*.md")):
    t = f.read_text(encoding="utf-8")
    has_block = bool(re.search(r'\^sec-', t))
    has_zotero_status = "zotero_status:" in t
    has_verification_status = "verification_status:" in t
    
    if has_block and not has_zotero_status:
        # Add zotero_status line after citekey or after the last existing status field
        if has_verification_status:
            t = t.replace(
                'verification_status: "✅ verified"',
                'verification_status: "✅ verified"\nzotero_status: verified'
            )
        else:
            # Insert after title or doi line
            t = re.sub(r'(doi:\s*"[^"]*")\n', r'\1\nzotero_status: verified\n', t)
        f.write_text(t, encoding='utf-8')
        fixed += 1
        ref_m = re.search(r'ref:\s*"\[(\d+)\]"', t)
        ref = ref_m.group(1) if ref_m else "?"
        print(f"  [{ref}] {f.stem}")

print(f"\nNormalized {fixed} notes.")
