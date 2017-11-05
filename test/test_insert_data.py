# -*- coding: utf-8 -*-
from db import dbMysql 
import MySQLdb

def insert_data_for_test(sqlList):
    db = dbMysql.db_conn
    dbCursor = db.cursor()
    for i in sqlList:
        try:
            dbCursor.execute(i)
        except MySQLdb.Error, e:
            print "execute [%s] failed!\n %s"%(i, e)
    db.commit()
    db.close()

if __name__ == "__main__":
    # sqlList = ['insert into users (name, passwd, email_address)\
    #             values ("%s","%s", "%s");' %("yinbin", '123456', 'yinbin@126.com'),
    #            'insert into users (name, passwd, email_address)\
    #             values ("%s","%s", "%s");' %("jiangjin", '123qwe', 'jiangjin@163.com'),
    #             'insert into users (name, passwd, email_address)\
    #             values ("%s","%s", "%s");' %("zhangzhi", '123456', 'zhangzhi@163.com'),
    #           ]
    sqlList = ['insert into devlist (name, asset_number, owner, being_user, ip_address, console_info, note)\
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
    insert_data_for_test(sqlList)
