#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2, urllib
import json
import sys

dest = 'http://127.0.0.1:50001/prelogin'
data = json.dumps({'addr_version': 'v1.016',
                   'soft_version':'v1.00'})
#data = 'abc'
req = urllib2.Request(dest, data)
#print urllib.urlencode({'data': data})
res = urllib2.urlopen(req) 
print res.info()
print res.read() 

