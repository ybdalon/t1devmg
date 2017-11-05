#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, time
import urllib2, cookielib


def login():
    data = json.dumps({'username': username, 'password':passwd})
    req = urllib2.Request(loginaddress, data)
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    res = urllib2.urlopen(req)
    print res.info()
    print res.read()

def loginout():
    pass


if __name__ == '__main__':
    username = 'yinbin'
    passwd = '123456'
    loginaddress = 'http://127.0.0.1:50001/login'
    loginoutaddress = 'http://127.0.0.1:50001/logout'

    login()