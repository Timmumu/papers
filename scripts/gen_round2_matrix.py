"""Phase 3 (revised): Generate Master Reference Index for ALL notes in 01_source/.
Output: LR 2round/LR_Matrix_PRISMA_section8.md
"""
import csv, re
from pathlib import Path
from collections import Counter

# --- 1. Read 2round748.csv for DOI lookup ---
doi_set = set()
with open('LR 2round/csv/2round748.csv', 'r', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        doi = (row.get('DOI') or '').strip().lower()
        if doi:
            doi_set.add(doi)

# --- 2. Read retained_for_fulltext.csv for screening vectors ---
retained = {}
with open('LR 2round/csv/retained_for_fulltext.csv', 'r', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        doi = (row.get('DOI') or '').strip().lower()
        if doi:
            retained[doi] = {
                'lens_id': row.get('Lens ID', ''),
                'title': (row.get('Title') or '').replace('\n', ' ').replace('\r', ' ')[:120],
                'year': row.get('Year', ''),
                'decision': row.get('Decision', ''),
                'v1_dt': (row.get('V1_DT') or '')[:60],
                'v2_aeco': (row.get('V2_AECO') or '')[:60],
                'v3_method': (row.get('V3_method') or '')[:60],
            }

# --- 3. Scan ALL 01_source notes ---
rows = []
for md in sorted(Path('01_source').glob('*.md')):
    t = md.read_text(encoding='utf-8')
    
    ident = 'databases' if 'identification: databases' in t else 'other methods'
    zs_m = re.search(r'zotero_status:\s*(\S+)', t)
    zs = zs_m.group(1) if zs_m else 'not-checked'
    ck_m = re.search(r'citekey:\s*"([^"]+)"', t)
    citekey = ck_m.group(1) if ck_m else md.stem
    auth_m = re.search(r'authors:\s*"([^"]*)"', t)
    authors = (auth_m.group(1) or '')[:60]
    yr_m = re.search(r'year:\s*(\d{4})', t)
    year = yr_m.group(1) if yr_m else ''
    doi_m = re.search(r'doi:\s*"?(10\.[^"\s\n]+)"?', t)
    doi = doi_m.group(1).strip().lower() if doi_m else ''
    zk_m = re.search(r'zotero_key:\s*"([^"]*)"', t)
    zk = zk_m.group(1) if zk_m else ''
    title_m = re.search(r'title:\s*"([^"]*)"', t)
    title = (title_m.group(1) or md.stem)[:100]
    title = title.replace('\n', ' ').replace('\r', ' ').replace('|', '/')
    ref_m = re.search(r'ref:\s*"\[(\d+)\]"', t)
    ref = ref_m.group(1) if ref_m else ''
    
    r = retained.get(doi, {})
    v1 = (r.get('v1_dt', '') or '')[:35]
    v2 = (r.get('v2_aeco', '') or '')[:35]
    v3 = (r.get('v3_method', '') or '')[:35]
    
    rows.append({
        'ref': ref, 'citekey': citekey, 'authors': authors, 'year': year,
        'title': title, 'zotero_key': zk[:8] if zk else '--',
        'zotero_status': zs, 'identification': ident,
        'v1_dt': v1, 'v2_aeco': v2, 'v3_method': v3,
    })

# --- 4. Statistics ---
ident_ctr = Counter(r['identification'] for r in rows)
status_ctr = Counter(r['zotero_status'] for r in rows)
year_ctr = Counter(r['year'] for r in rows)

# --- 5. Generate markdown ---
out = []
out.append('## 8. Master Reference Index -- All Atomic Notes (n = {})'.format(len(rows)))
out.append('')
out.append('> Auto-generated from `01_source/*.md` frontmatter. All {} notes indexed.'.format(len(rows)))
out.append('> **Identification:** `databases` = DOI in Lens.org export (n = {}); `other methods` = round-1 corpus, snowballing, supplementary (n = {}).'.format(
    ident_ctr.get('databases', 0), ident_ctr.get('other methods', 0)))
out.append('')
out.append('**Identification:** databases = {}, other methods = {} (total {})'.format(
    ident_ctr.get('databases', 0), ident_ctr.get('other methods', 0), len(rows)))
out.append('')
out.append('**Zotero status:** {}'.format(dict(status_ctr)))
out.append('')
out.append('**Year distribution:** {}'.format(dict(sorted(year_ctr.items()))))
out.append('')

out.append('| # | Ref | Citekey | Authors | Year | Title | Zotero | Status | Ident | V1 (DT) | V2 (AECO) | V3 (Method) |')
out.append('|:---:|:---:|---|---|:---:|---|---|:---:|:---:|---|---|---|')

for i, r in enumerate(sorted(rows, key=lambda x: x['citekey'].lower()), 1):
    out.append(
        '| {} | [{}] | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |'.format(
            i, r['ref'], r['citekey'], r['authors'][:45], r['year'],
            r['title'][:70], r['zotero_key'], r['zotero_status'],
            r['identification'], r['v1_dt'][:25], r['v2_aeco'][:25], r['v3_method'][:25]
        )
    )

out.append('')
out.append('> **Total:** {} notes. databases = {}, other methods = {}.'.format(
    len(rows), ident_ctr.get('databases', 0), ident_ctr.get('other methods', 0)))

# Write
output_path = Path('LR 2round/LR_Matrix_PRISMA_section8.md')
output_path.write_text('\n'.join(out), encoding='utf-8')
print('Written: {} ({} lines, {} chars)'.format(output_path, len(out), len('\n'.join(out))))
print('Identification: {}'.format(dict(ident_ctr)))
print('Status: {}'.format(dict(status_ctr)))
