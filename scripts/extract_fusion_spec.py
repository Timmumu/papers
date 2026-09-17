# -*- coding: utf-8 -*-
"""Extract the user's fusion-depth spec message from the session transcript."""
import json, re

P = r'c:\Users\41981\AppData\Roaming\Code\User\workspaceStorage\0a22beb9c94f0ac03ed7d6533b87ad49\GitHub.copilot-chat\transcripts\588734bc-f0b8-44c7-9086-14cb915a35ed.jsonl'
out = []
with open(P, encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        if 9600 <= i <= 9700:
            try:
                obj = json.loads(line)
            except Exception:
                continue
            t = obj.get('type')
            if t == 'user.message':
                content = obj.get('data', {}).get('content')
                if isinstance(content, str) and ('Fusion' in content or 'AC1' in content or 'fusion' in content):
                    out.append('=== LINE %d (user) ===' % i)
                    out.append(content)
            elif t == 'assistant.message':
                content = obj.get('data', {}).get('content')
                if isinstance(content, str) and 'Fusion depth' in content:
                    out.append('=== LINE %d (assistant) ===' % i)
                    out.append(content[:2000])
with open(r'h:\phd\6.pjt\LR1\papers\scripts\_spec_extract.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
print('wrote', len(out), 'blocks')
