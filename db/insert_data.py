#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dbMysql import *


def insert_data_for_test(dbcon, sqlList):
    dbCursor = dbcon.cursor()
    for i in sqlList:
        try:
            dbCursor.execute(i)
        except MySQLdb.Error, e:
            print "execute [%s] failed!\n %s"%(i, e)
    dbcon.commit()

sqlList_user = ['insert into users (name, passwd, email_address)\
            values ("%s","%s", "%s");' %("admin", 't1networks', 't1test@.com'),
           'insert into users (name, passwd, email_address)\
            values ("%s","%s", "%s");' %("yinbin", '123456', 'yinbin@t1networks.com'),
           'insert into users (name, passwd, email_address)\
            values ("%s","%s", "%s");' %("panlei", '123456', 'panlei@t1networks.com'),
            'insert into users (name, passwd, email_address)\
            values ("%s","%s", "%s");' %("liuhao", '123456', 'liuhao@t1networks.com'),
            'insert into users (name, passwd, email_address)\
            values ("%s","%s", "%s");' % ("wudong", '123456', 'wudong@t1networks.com'),
            'insert into users (name, passwd, email_address)\
            values ("%s","%s", "%s");' % ("wangboyuan", '123456', 'wangboyuan@t1networks.com'),
            'insert into users (name, passwd, email_address)\
            values ("%s","%s", "%s");' % ("zhangxian", '123456', 'zhangxian@t1networks.com'),
          ]
sqlList_test = ['insert into devlist (name, asset_number, owner, being_user, ip_address, console_info, note)\
                values ("%s","%s", "%s", "%s","%s", "%s", "%s");' % (
           "lihua", 't1-ad-10', 'yinbin', 'wangboyuan', '1.1.1.2', '192.168.10.13:33', 'this is yb dut'),
           'insert into devlist (name, asset_number, owner, being_user, ip_address, console_info, note)\
            values ("%s","%s", "%s", "%s","%s", "%s", "%s");' % (
           u"xinhan", 't1-ad-11', 'wangboyuan', 'wangboyuan', '1.4.1.2', '192.168.10.13:23',
           'this is wangboyuan dut'),
           'insert into devlist (name, asset_number, owner, being_user, ip_address, console_info, note)\
            values ("%s","%s", "%s", "%s","%s", "%s", "%s");' % (
           u"lihua", 't1-ad-10', 'zhangxian', 'zhangxian', '1.1.15.0', '192.168.10.13:53', 'this is yb dut'),
           'insert into devlist (name, asset_number, owner, being_user, ip_address, console_info, note)\
           values ("%s","%s", "%s", "%s","%s", "%s", "%s");' % (
           u"lihua", 't1-ad-10', 'liuhao', 'wangboyuan--------', '1.1.1.2', 'console 192.168.10.13:33',
           'this is yb dut, asdfasdfasdfasdfasdfadfasdfasdfasdfasdfasdfasdf'),
           'insert into devlist (name, asset_number, owner, being_user, ip_address, console_info, note)\
           values ("%s","%s", "%s", "%s","%s", "%s", "%s");' % (
           u"lihua", 't1-ad-10', 'wudong', 'wangboyuan', '1.1.1.2', '192.168.10.13:33', 'this is yb dut'),
           'insert into devlist (name, asset_number, owner, being_user, ip_address, console_info, note)\
           values ("%s","%s", "%s", "%s","%s", "%s", "%s");' % (
           u"lihua", 't1-ad-10', 'panlei', 'wangboyuan', '1.1.1.2', '192.168.10.13:33', 'this is yb dut'),
           ]
sqlList_devtype = ['insert into devtype (typename, note) values ("%s", "%s") '%('PC', "PC"),
                   'insert into devtype (typename, note) values ("%s", "%s") ' % ('dut', "DUT")]

dbconn = connect_db()
insert_data_for_test(dbconn, sqlList_user)
insert_data_for_test(dbconn, sqlList_test)
insert_data_for_test(dbconn, sqlList_devtype)
dbconn.close()