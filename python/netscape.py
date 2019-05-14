#!/usr/bin/env python3
"""a simple http client | Author: chris.marquardt2@verizonwireless.com"""

import http.client

PORT = 8000

conn = http.client.HTTPConnection("localhost", PORT)

conn.request('HEAD', '/')

res = conn.getresponse()
print(dir(res))
print(res.status, res.reason)

conn.request('GET', '/')
res = getresponse()
print(res.status, res.reason)

