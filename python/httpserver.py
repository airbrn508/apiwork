#!/usr/bin/env python3
"""Building a simple HTTP server | Author: chris.marquardt2@verizonwireless.com
https://docs.python.org/3/library/http.server.html"""

import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


