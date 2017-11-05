#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2, urllib
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#dest = 'http://120.131.132.250:50001/register'
dest = 'http://127.0.0.1:50001/register'
data = json.dumps({'username': 'zhangzhi',
                   'password':'123456',
                   'secret':'dfasdfsa',
                   'area':'云南.昆明.西山.L街.B社区.cc小区'}) 
#data = 'abc'
req = urllib2.Request(dest, data)
#print urllib.urlencode({'data': data})
res = urllib2.urlopen(req) 
print res.info()
print res.read() 

