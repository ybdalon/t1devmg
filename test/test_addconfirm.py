#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2, urllib
import json
import sys

#dest = 'http://120.131.132.250:50001/addconfirm'
dest = 'http://127.0.0.1:50001/addconfirm'
data = json.dumps({'username':'yinbin','frdname':'zhangzhi','content':'','pass':'1'})
#data = 'abc'
req = urllib2.Request(dest, data)
#print urllib.urlencode({'data': data})
res = urllib2.urlopen(req)
print res.info()
print res.read()