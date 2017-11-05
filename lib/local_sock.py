#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, time, json
import json, urllib

def tcp_conn_sendstr(target, sendstr):
    try:
        sc = socket.create_connection(target, timeout= 10)
    except:
        print "connect to %s failed!"%(target, )
    sc.send(sendstr)
    data = ''
    while 1:
        try:
            data += sc.recv(1024)
        except:
            print "lib.local_sock: maybe recv timeout!"
            break
        if not data:
            break
    sc.close()
    return data

def get_sock2imserver():
    imserveraddr = ('127.0.0.1', 60001)
    try:
        sc = socket.create_connection(imserveraddr, timeout= 10)
    except:
        print "connect to %s failed!"%(imserveraddr, )
        return
    return sc

def msg_to_imserver(sock, sender, reciver, title, content, content_img, msg_type):
    msg = {'sender':sender,
           'receiver':reciver,
           'sendTime':time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),       #xxxx-xx-xx xx:xx:xx
           'receiveTime':time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
           'title':title,                   #群消息复用此字段，存放groupid
           'content':content,
           'content_img':content_img,
           'msg_type':msg_type}            #0登陆，1表示群信息，2表示私聊，3好友请求，4好友请求的回应，5注销
    res = (json.dumps(msg)).encode('utf8')
    sock.send(res+'\r\n')

def test_con2imserver():
    target = ('127.0.0.1', 60001)
    sendstr = '...'
    tcp_conn_sendstr(target, sendstr)



if __name__ == '__main__':
    pass
    sock = get_sock2imserver()
    msg_to_imserver(sock, '', '', '', '只能', '', 1)
