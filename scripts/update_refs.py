"""Safely update LR_GPT.md: mark removed refs, update citations, fix bare wikilinks."""
from pathlib import Path
import re

LR = Path("MD/LR_GPT.md")
text = LR.read_text(encoding="utf-8")

parts = text.split("## 8. References", 1)
if len(parts) != 2:
    print("ERROR: cannot split")
    exit(1)
body, refs = parts

# PART 1: Mark removed references
removed = [35, 41, 42, 45, 46, 48, 50, 59, 60, 68]
for r in removed:
    refs = re.sub(rf"^\[{r}\]\s", f"[{r}] ~~REMOVED~~ ", refs, flags=re.MULTILINE)

# PART 2: Update narrative citations
body = body.replace('[35] [[Ayyalasomayajula2022]]', '[95]')
body = body.replace('[35],', '')
body = body.replace('[59] [[al.2022]]', '')
body = body.replace('[41] [[Olofsson2010]]', '[101]')
body = body.replace('[68] [[Akinci2021]]', '[92],[93],[94]')
body = body.replace('[60] [[Bolpagni2022]]', '[96]')
body = body.replace(', [42] [[Borrmann2018]]', '')
body = body.replace(', [48] [[Bedford2001]]', '')
body = body.replace(', [50] [[Eastman2018]]', '')
body = body.replace('[45] [[Li2021]]', '[97]')
body = body.replace('[46] [[Burch2012]]', '[100]')

# Clean up double commas
body = body.replace(', ,', ',')

# PART 3: Fix bare wikilinks → block ID for verified papers
bare_fixes = {
    '[[Schleich2017]]': '[[Schleich2017#^sec-abstract]]',
    '[[Singh2021]]': '[[Singh2021#^sec-abstract]]',
    '[[Opoku2021]]': '[[Opoku2021#^sec-abstract]]',
    '[[Tao2019]]': '[[Tao2019#^sec-abstract]]',
    '[[Rasheed2020]]': '[[Rasheed2020#^sec-abstract]]',
    '[[Jones2020]]': '[[Jones2020#^sec-abstract]]',
    '[[Sepasgozar2021]]': '[[Sepasgozar2021#^sec-abstract]]',
    '[[Ozturk2021]]': '[[Ozturk2021#^sec-abstract]]',
    '[[Omrany2023]]': '[[Omrany2023#^sec-abstract]]',
    '[[Greif2020]]': '[[Greif2020#^sec-abstract]]',
    '[[Lee2021]]': '[[Lee2021#^sec-abstract]]',
    '[[Jiang2022]]': '[[Jiang2022#^sec-abstract]]',
    '[[Ruppert2018]]': '[[Ruppert2018#^sec-abstract]]',
    '[[Qi2021]]': '[[Qi2021#^sec-abstract]]',
    '[[Shahzad2022]]': '[[Shahzad2022#^sec-abstract]]',
    '[[Chen2021]]': '[[Chen2021#^sec-abstract]]',
    '[[Hakimi2024]]': '[[Hakimi2024#^sec-abstract]]',
    '[[Hosamo2022b]]': '[[Hosamo2022b#^sec-abstract]]',
}
for old, new in bare_fixes.items():
    body = body.replace(old, new)

text = body + "## 8. References" + refs
LR.write_text(text, encoding="utf-8")
print("Done.")
