# -*- coding: utf-8 -*-
"""Audit LR4 Step-3 rows against locally readable full-text files.

This does not change coding decisions. It verifies whether each row currently
rendered in the Step-3 matrix has a canonical local PDF/TXT companion in
04d_LR4/4. fulltext L2, and writes reproducible audit artifacts.
"""
import csv
import json
import os
import re
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))

import step3_lr4_data  # noqa: E402

SS = os.path.join(ROOT, '04d_LR4', '5. SLR matrix', 'ss')
L2 = os.path.join(ROOT, '04d_LR4', '4. fulltext L2')
L1 = os.path.join(ROOT, '04d_LR4', '3. fulltext L1')
OUT_JSON = os.path.join(SS, 'step3_fulltext_audit.json')
OUT_CSV = os.path.join(SS, 'step3_fulltext_audit.csv')
OUT_MD = os.path.join(SS, 'step3_fulltext_audit.md')

with open(os.path.join(SS, 'corpus_lr4.json'), encoding='utf-8') as fh:
    CORPUS = {int(r['row']): r for r in json.load(fh)}


def esc_md(value):
    return re.sub(r'\s+', ' ', str(value or '')).replace('|', '/').strip()


def local_files(base_dir, row):
    prefix = 'R%03d' % row
    txt_dir = os.path.join(base_dir, 'txt')
    pdfs = [f for f in os.listdir(base_dir) if f.lower().endswith('.pdf') and f.startswith(prefix)] if os.path.isdir(base_dir) else []
    txts = [f for f in os.listdir(txt_dir) if f.lower().endswith('.txt') and f.startswith(prefix)] if os.path.isdir(txt_dir) else []
    return sorted(pdfs), sorted(txts)


def txt_state(base_dir, txts):
    if not txts:
        return 'missing', 0
    txt_dir = os.path.join(base_dir, 'txt')
    sizes = []
    for name in txts:
        path = os.path.join(txt_dir, name)
        try:
            sizes.append(os.path.getsize(path))
        except OSError:
            sizes.append(0)
    size = max(sizes) if sizes else 0
    if size >= 2000:
        return 'readable', size
    if size > 0:
        return 'too-short', size
    return 'empty', size


def evidence_state(row):
    checked = []
    for tier, base_dir in [('L2', L2), ('L1', L1)]:
        pdfs, txts = local_files(base_dir, row)
        state, txt_size = txt_state(base_dir, txts)
        checked.append((tier, pdfs, txts, state, txt_size))
        if pdfs and state == 'readable':
            return 'local-readable-fulltext', tier, pdfs, txts, state, txt_size, checked
    for tier, pdfs, txts, state, txt_size in checked:
        if pdfs:
            return 'local-pdf-not-readable', tier, pdfs, txts, state, txt_size, checked
    return 'no-local-fulltext', '', [], [], 'missing', 0, checked


rows = []
for row in sorted(step3_lr4_data.S3L):
    rec = CORPUS.get(row, {})
    values = step3_lr4_data.S3L[row]
    p, q, r = values[:3]
    source = values[15] if len(values) > 15 else ''
    audit_status, evidence_tier, pdfs, txts, state, txt_size, checked = evidence_state(row)
    rows.append({
        'row': row,
        'title': rec.get('title', ''),
        'year': rec.get('year', ''),
        'doi': rec.get('doi', ''),
        'stage2': ''.join((p, q, r)),
        'step3_decision': 'full-coded' if (p, q, r) == ('Yes', 'Yes', 'Yes') else 'stage2-excluded',
        'source_tag': source,
        'audit_status': audit_status,
        'evidence_tier': evidence_tier,
        'pdf_files': pdfs,
        'txt_files': txts,
        'txt_state': state,
        'txt_size': txt_size,
        'checked_locations': [
            {'tier': tier, 'pdf_files': cpdfs, 'txt_files': ctxts, 'txt_state': cstate, 'txt_size': csize}
            for tier, cpdfs, ctxts, cstate, csize in checked
        ],
    })

pending_rows = []
for row in sorted(getattr(step3_lr4_data, 'STRICT_FULLTEXT_PENDING_DATA', {})):
    rec = CORPUS.get(row, {})
    values = step3_lr4_data.STRICT_FULLTEXT_PENDING_DATA[row]
    p, q, r = values[:3]
    source = values[15] if len(values) > 15 else ''
    audit_status, evidence_tier, pdfs, txts, state, txt_size, checked = evidence_state(row)
    pending_rows.append({
        'row': row,
        'title': rec.get('title', ''),
        'year': rec.get('year', ''),
        'doi': rec.get('doi', ''),
        'stage2': ''.join((p, q, r)),
        'step3_decision': 'full-coded' if (p, q, r) == ('Yes', 'Yes', 'Yes') else 'stage2-excluded',
        'source_tag': source,
        'audit_status': audit_status,
        'evidence_tier': evidence_tier,
        'pdf_files': pdfs,
        'txt_files': txts,
        'txt_state': state,
        'txt_size': txt_size,
        'checked_locations': [
            {'tier': tier, 'pdf_files': cpdfs, 'txt_files': ctxts, 'txt_state': cstate, 'txt_size': csize}
            for tier, cpdfs, ctxts, cstate, csize in checked
        ],
    })

summary = {
    'coded_rows': len(rows),
    'full_coded_rows': sum(1 for row in rows if row['step3_decision'] == 'full-coded'),
    'stage2_excluded_rows': sum(1 for row in rows if row['step3_decision'] == 'stage2-excluded'),
    'strict_pending_rows': len(pending_rows),
    'strict_pending_status_counts': dict(Counter(row['audit_status'] for row in pending_rows)),
    'audit_status_counts': dict(Counter(row['audit_status'] for row in rows)),
    'evidence_tier_counts': dict(Counter(row['evidence_tier'] or 'missing' for row in rows)),
    'source_tag_counts': dict(Counter(row['source_tag'] for row in rows)),
    'source_by_audit_status': {
        source: dict(Counter(row['audit_status'] for row in group))
        for source, group in defaultdict(list, {
            source: [row for row in rows if row['source_tag'] == source]
            for source in sorted(set(row['source_tag'] for row in rows))
        }).items()
    },
}

with open(OUT_JSON, 'w', encoding='utf-8') as fh:
    json.dump({'summary': summary, 'rows': rows, 'strict_pending_rows': pending_rows}, fh, ensure_ascii=False, indent=1)

with open(OUT_CSV, 'w', encoding='utf-8', newline='') as fh:
    fieldnames = ['row', 'year', 'step3_decision', 'source_tag', 'audit_status', 'evidence_tier', 'txt_state', 'txt_size', 'pdf_files', 'txt_files', 'doi', 'title']
    writer = csv.DictWriter(fh, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        out = dict(row)
        out['pdf_files'] = '; '.join(row['pdf_files'])
        out['txt_files'] = '; '.join(row['txt_files'])
        writer.writerow({key: out.get(key, '') for key in fieldnames})

missing = [row for row in rows if row['audit_status'] != 'local-readable-fulltext']
lines = [
    '# LR4 Step-3 Full-Text Audit',
    '',
    'Strict criterion: a Step-3 row is locally auditable only when a canonical `R###...pdf` and a readable `txt/R###...txt` companion are both present in either `04d_LR4/4. fulltext L2` or the earlier verified staging folder `04d_LR4/3. fulltext L1`.',
    '',
    '## Summary',
    '',
]
for key, value in summary.items():
    lines.append('- %s: `%s`' % (key, value))
lines.extend([
    '',
    '## Rows Requiring Full-Text Evidence',
    '',
    '| ID | Source tag | Decision | Audit status | Evidence tier | DOI | Title |',
    '| --- | --- | --- | --- | --- | --- | --- |',
])
for row in missing:
    lines.append('| R%03d | %s | %s | %s | %s | %s | %s |' % (
        row['row'], esc_md(row['source_tag']), esc_md(row['step3_decision']),
        esc_md(row['audit_status']), esc_md(row['evidence_tier']), esc_md(row['doi']), esc_md(row['title'])))

lines.extend([
    '',
    '## Strict-Pending Rows Removed From Active Coding',
    '',
    '| ID | Source tag | Prior decision | Audit status | DOI | Title |',
    '| --- | --- | --- | --- | --- | --- |',
])
for row in pending_rows:
    lines.append('| R%03d | %s | %s | %s | %s | %s |' % (
        row['row'], esc_md(row['source_tag']), esc_md(row['step3_decision']),
        esc_md(row['audit_status']), esc_md(row['doi']), esc_md(row['title'])))

with open(OUT_MD, 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(lines) + '\n')

print('wrote', OUT_JSON)
print('wrote', OUT_CSV)
print('wrote', OUT_MD)
print(json.dumps(summary, ensure_ascii=False, indent=1))