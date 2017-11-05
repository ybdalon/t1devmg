#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2, urllib, cookielib
import json
import sys

def test_chgpass():
    dest0 = 'http://127.0.0.1:50001/login'
    dest1 = 'http://127.0.0.1:50001/changepwd'
    data0 = json.dumps({'username': 'yinbin', 'password':'123456'})
    data1 = json.dumps({'username': 'yinbin', 
                        'oldpassword':'123456', 
                        'newpassword':'123456'})
    cj = cookielib.CookieJar() 
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    req0 = urllib2.Request(dest0, data0)
    res0 = opener.open(req0) 
    print res0.info()
    print res0.read()
    print '----------------------------'
    req1 = urllib2.Request(dest1, data1)
    res1 = opener.open(req1) 
    print res1.info()
    print res1.read() 
    

if __name__=='__main__':
    test_chgpass()