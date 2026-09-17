# -*- coding: utf-8 -*-
"""LR4 Step-1 screening store: merges screening_lr4_b01..b13 into S4.

S4[rownum] = (G, H, I, J, K, note)  for rownum in 1..956.
Decision derived: Include iff all five flags == 'Yes'.
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))

S4 = {}
for i in range(1, 14):
    name = 'screening_lr4_b%02d' % i
    path = os.path.join(HERE, name + '.py')
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for r, t in mod.SB.items():
        assert len(t) == 6, (name, r)
        assert all(f in ('Yes', 'No') for f in t[:5]), (name, r, t)
        assert r not in S4, ('duplicate row', r)
        S4[r] = tuple(t)

assert len(S4) == 956, len(S4)
assert all(r in S4 for r in range(1, 957))

def decision(flags):
    return 'Include' if all(f == 'Yes' for f in flags) else 'Exclude'

if __name__ == '__main__':
    inc = [r for r, t in sorted(S4.items()) if decision(t[:5]) == 'Include']
    print('rows=%d includes=%d' % (len(S4), len(inc)))
    print('include rows:', inc)
