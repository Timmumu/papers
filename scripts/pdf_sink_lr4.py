# -*- coding: utf-8 -*-
"""Local PDF sink: receives PDF bytes POSTed by the integrated browser and
writes them to the LR4 fulltext staging folder.
Usage: .venv\\Scripts\\python.exe scripts/pdf_sink_lr4.py [port]
"""
import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

ROOT = r'H:\phd\6.pjt\LR1\papers'
OUT = os.path.join(ROOT, '04d_LR4', '4. fulltext L2')
os.makedirs(OUT, exist_ok=True)
LOG = os.path.join(ROOT, '04d_LR4', '5. SLR matrix', 'ss', 'browser_dl_log.txt')


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self._cors()
        self.end_headers()
        self.wfile.write(b'sink-ok')

    def do_POST(self):
        q = self.path.split('?', 1)[1] if '?' in self.path else ''
        name = ''
        for kv in q.split('&'):
            if kv.startswith('name='):
                import urllib.parse
                name = urllib.parse.unquote(kv[5:])
        n = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(n)
        status = 'saved'
        if not name or not name.endswith('.pdf'):
            status = 'bad-name'
            name = 'bad.pdf'
        if len(body) < 15000:
            status = 'too-small(%d)' % len(body)
        if not body.startswith(b'%PDF'):
            status = 'not-pdf-magic(%r)' % body[:8]
        path = os.path.join(OUT, os.path.basename(name))
        if status == 'saved':
            with open(path, 'wb') as f:
                f.write(body)
        with open(LOG, 'a', encoding='utf-8') as f:
            f.write('%s\t%s\t%d\n' % (status, name, len(body)))
        self.send_response(200)
        self._cors()
        self.end_headers()
        self.wfile.write(status.encode())


if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    srv = HTTPServer(('127.0.0.1', port), H)
    print('pdf-sink listening on 127.0.0.1:%d -> %s' % (port, OUT))
    srv.serve_forever()
