"""Fix misplaced Step-3 rows in the SLR summary matrix.

The insert_matrix_batch3.py script used mat.find('| 3906 |') which matched
the FIRST occurrence of that pattern (Step-1 table row '| 74  | 3906 |'),
so the 25 new Step-3 rows were inserted at lines ~89-114 in the middle of
the Step-1 table.

This script:
1. Locates the misplaced block (25 Step-3 rows) and removes it.
2. Locates the true Step-3 table (after '## Step 3 Deep-Read Coding' heading)
   and inserts the 25 rows after the last existing Step-3 row (3906).
"""
import re
import sys

PATH = r"h:\phd\6.pjt\LR1\papers\04c_LR 3round\SLR summary matrix.md"

def main():
    with open(PATH, encoding="utf-8") as f:
        text = f.read()
    lines = text.splitlines()

    # ---- 1. Locate the misplaced block ----
    # The block is: lines after Step-1 row '| 74  | 3906 |' and before '| 75  | 3921 |'
    # We find the index of the Step-1 3906 row (must start with '| 74  | 3906 |')
    anchor_idx = None
    for i, l in enumerate(lines):
        if l.startswith("| 74  | 3906 |"):
            anchor_idx = i
            break
    if anchor_idx is None:
        print("ERROR: Step-1 anchor '| 74  | 3906 |' not found")
        sys.exit(1)

    # Collect rows that are Step-3 style immediately after anchor (skip blank)
    block_start = anchor_idx + 1
    # expect a blank line then 25 Step-3 rows
    if lines[block_start].strip() != "":
        print("ERROR: expected blank line after Step-1 3906 row")
        sys.exit(1)
    block_rows = []
    i = block_start + 1
    while i < len(lines) and re.match(r"^\|\s*\d{4}\s*\|", lines[i]):
        block_rows.append(lines[i])
        i += 1
    print(f"Found misplaced block with {len(block_rows)} Step-3 rows at lines {block_start+2}..{i}")

    if len(block_rows) != 25:
        print(f"WARNING: expected 25 rows, found {len(block_rows)}")

    # Remove the misplaced block (including its preceding blank line)
    del lines[block_start:i]

    # ---- 2. Locate the Step-3 table ----
    step3_heading_idx = None
    for j, l in enumerate(lines):
        if l.startswith("## Step 3 Deep-Read Coding"):
            step3_heading_idx = j
            break
    if step3_heading_idx is None:
        print("ERROR: '## Step 3 Deep-Read Coding' heading not found")
        sys.exit(1)

    # Find the last existing Step-3 data row (starts with '| <rid> |' after the header)
    # The Step-3 table header has columns ID/P/Q/R/U Tier/... We find the 3906 row.
    last_data_idx = None
    for k in range(step3_heading_idx, len(lines)):
        if re.match(r"^\|\s*3906\s*\|", lines[k]):
            last_data_idx = k
    if last_data_idx is None:
        print("ERROR: Step-3 3906 row not found")
        sys.exit(1)
    print(f"Step-3 3906 row at line {last_data_idx+1}")

    # Insert block_rows after the 3906 row
    insert_at = last_data_idx + 1
    new_lines = lines[:insert_at] + block_rows + lines[insert_at:]

    with open(PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))

    print(f"Done. Moved {len(block_rows)} rows to after Step-3 row 3906 (line {insert_at+1}).")
    print(f"Total lines now: {len(new_lines)}")

if __name__ == "__main__":
    main()
