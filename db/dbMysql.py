#!/usr/bin/env python
# -*- coding:utf-8 -*-

import MySQLdb

#请按下面参数来配置好数据库环境
MYSQL_CONN = None
HOST = '192.168.10.110'
USERNAME = 'devadmin'
PASSWD = 'devpasswd'
DATABASENAME = 't1devmg'
CHARSET = 'utf8'

def connect_db():
    try:
        dbconn = MySQLdb.connect(host=HOST, port=3306, user=USERNAME, passwd=PASSWD, db=DATABASENAME, charset=CHARSET)
    except Exception, e:
        print "connect to database %s failed, reason:%s\n"%(DATABASENAME, e)
        return None
    return dbconn

class mydb(object):
    def __init__(self, host, port, user, passwd, db):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.dbConnections =  None
        self.create_conns()
        self.check_thread()
    def create_conns(self):
        try:
            self.dbConnections = MySQLdb.connect(host=self.host, port=self.port,
                                                 user=self.user, passwd=self.passwd, db=self.db, charset='utf8')
        except Exception, e:
            print "connect to database %s failed, reason:%s\n"%(DATABASENAME, e)
    def db_conn_check(self, interval = 10):
        import time
        while 1:
            try:
                cursor = self.dbConnections.cursor()
                cursor.execute('show databases')
                cursor.close()
                #print '[YB record：check DB connect ok]'
            except Exception, e:
                print '[YB record check DB connect failed]', e
                self.create_conns()
            time.sleep(interval)
    def check_thread(self):
        import threading
        t = threading.Thread(target = self.db_conn_check)
        t.setDaemon(1)
        t.start()
    def get_one_conn(self):
        return self.dbConnections

my_db = mydb(HOST, 3306, USERNAME, PASSWD, DATABASENAME)


if __name__ == '__main__':
    connect_db()


