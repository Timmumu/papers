"""Copy + extract + verify one Endnote PDF by filename."""
import os, sys, shutil, subprocess
fname = sys.argv[1]
rid = sys.argv[2]
slug = sys.argv[3]
doi = sys.argv[4].lower()
EN_PDF = r'H:\phd\paper\Endnote\My EndNote Library.Data\PDF'
FT = r'h:\phd\6.pjt\LR1\papers\04c_LR 3round\ss\fulltext'
PWSH = r'h:/phd/6.pjt/LR1/papers/.venv/Scripts/python.exe'
src = None
for root, _, fs in os.walk(EN_PDF):
    if fname in fs:
        src = os.path.join(root, fname)
        break
if not src:
    print('SRC NOT FOUND')
    sys.exit(1)
print('src:', src)
out_pdf = os.path.join(FT, f'{rid}_{slug}.pdf')
out_txt = os.path.join(FT, f'{rid}_{slug}.txt')
shutil.copy2(src, out_pdf)
code = (f'from pypdf import PdfReader; r=PdfReader(r"{out_pdf}"); '
        f'open(r"{out_txt}","w",encoding="utf-8").write("\\n".join(p.extract_text() or "" for p in r.pages))')
subprocess.run([PWSH, '-c', code], capture_output=True, text=True, timeout=180)
c = open(out_txt, encoding='utf-8', errors='replace').read()
print('len', len(c), 'doi-ok', doi in c[:4500].lower())
