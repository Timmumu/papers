# -*- coding: utf-8 -*-
"""Peek at a per-paper coding extract, wrapped and windowed.
Usage: .venv\\Scripts\\python.exe scripts/peek_lr4.py R055 [start] [len]
"""
import sys
import textwrap

row = sys.argv[1]
start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
length = int(sys.argv[3]) if len(sys.argv) > 3 else 6000
p = '04d_LR4/5. SLR matrix/ss/coding/_one/%s.txt' % row
t = open(p, encoding='utf-8', errors='replace').read()
seg = t[start:start + length]
print(textwrap.fill(seg, 120))
print('--- [%s] chars %d..%d of %d' % (row, start, start + length, len(t)))
