#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

def tcp_conn(target, sendlist):
    try:
        sc = socket.create_connection(target, timeout= 10)
    except:
        print "connect to %s failed!"%(target, )
    for l in sendlist:
        sc.send(l)
        sc.recv(1024)
    sc.close()

if __name__ == '__main__':
    target = ('127.0.0.1', 800)
    sendlist = ['a', 'b']
    tcp_conn(target, sendlist)