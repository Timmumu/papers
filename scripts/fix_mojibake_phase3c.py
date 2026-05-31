"""
Reverse mojibake: text was originally UTF-8 dashes (en/em) followed by ASCII,
read as cp936 producing U+9225 + CJK char sequences.

Reverse: re-encode each U+9225+next-char pair as cp936 bytes, then decode as UTF-8.
"""
import os

TARGETS = ["Teo2005","Choi2021","Akinci2002","Akinci2021","Degani2024",
           "Fang2022-69","Hamel2024","Li2021","Love2014","Matthews2021",
           "Tixier2016","Zhang2041"]

def fix(text: str):
    out = []
    i = 0
    n_fixed = 0
    while i < len(text):
        ch = text[i]
        if ch == "\u9225" and i + 1 < len(text):
            nxt = text[i+1]
            try:
                seq = (ch + nxt).encode("cp936")
                if len(seq) == 4:
                    decoded = seq.decode("utf-8")
                    out.append(decoded)
                    n_fixed += 1
                    i += 2
                    continue
            except (UnicodeEncodeError, UnicodeDecodeError):
                pass
            if nxt == "?":
                # em-dash where second byte unmappable
                out.append("\u2014 ")
                n_fixed += 1
                i += 2
                continue
        out.append(ch)
        i += 1
    return "".join(out), n_fixed

for name in TARGETS:
    path = os.path.join("01_source", name + ".md")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    new, n = fix(text)
    if n:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(new)
        print(f"FIX {name}: {n} sequences")
    else:
        print(f"OK  {name}")
