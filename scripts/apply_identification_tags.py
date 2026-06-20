"""Phase 1.7: Batch apply identification: databases|other_methods tags to all 01_source notes."""
import csv
import re
from pathlib import Path

# --- 1. Build DOI lookup from 2round748.csv ---
doi_set = set()
with open('LR 2round/csv/2round748.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        doi = row.get('DOI', '').strip().lower()
        if doi:
            doi_set.add(doi)

SRC = Path('01_source')
tag_db = 'identification: databases'
tag_other = 'identification: other methods'

updated = 0
skipped = 0
errors = 0

for md in sorted(SRC.glob('*.md')):
    text = md.read_text(encoding='utf-8')
    
    # Check if already tagged
    if tag_db in text or tag_other in text:
        skipped += 1
        continue
    
    # Determine identification type
    doi_m = re.search(r'doi:\s*"?(10\.[^"\s\n]+)"?', text)
    doi = doi_m.group(1).strip().lower() if doi_m else ''
    
    if doi and doi in doi_set:
        new_tag = tag_db
    else:
        new_tag = tag_other
    
    # Apply the tag to the frontmatter tags field
    # Handle two YAML tag formats:
    # Format A: tags: ["tag1", "tag2", ...]
    # Format B: tags:\n  - tag1\n  - tag2
    
    if re.search(r'tags:\s*\[', text):
        # Format A: inline JSON-style list
        new_text = re.sub(
            r'(tags:\s*\[)([^\]]*)\]',
            lambda m: m.group(1) + m.group(2) + (', ' if m.group(2).strip() else '') + f'"{new_tag}"]',
            text,
            count=1
        )
    elif re.search(r'tags:\s*\n', text):
        # Format B: block style with hyphens
        # Find the tags section and add new tag before the next YAML key or ---
        new_text = re.sub(
            r'(tags:\s*\n(?:\s+-\s+[^\n]+\n)+)',
            lambda m: m.group(1).rstrip('\n') + f'\n  - {new_tag}\n',
            text,
            count=1
        )
    else:
        print(f'WARNING: Cannot parse tags in {md.name}')
        errors += 1
        continue
    
    if new_text != text:
        md.write_text(new_text, encoding='utf-8')
        updated += 1
        print(f'  {md.name}: +{new_tag}')
    else:
        skipped += 1

print(f'\n=== Tag Application Complete ===')
print(f'Updated: {updated}')
print(f'Skipped (already tagged or no change): {skipped}')
print(f'Errors: {errors}')
