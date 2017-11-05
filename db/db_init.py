#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dbMysql import * 


#创建用户表
userInfoTable = ('users',
                 'id INT(11) NOT NULL primary key AUTO_INCREMENT,'
                 'name VARCHAR(30) NOT NULL UNIQUE,'
                 'passwd VARCHAR(16) NOT NULL,'
                 'email_address VARCHAR(255) NOT NULL,'
                 'avatar VARCHAR(100),'
                 'imgpath VARCHAR(128) DEFAULT "",'
                 'userinfo text')
#创建登录审计信息表
loginRecordTable = ('login_record',
                    'username CHAR(30) NOT NULL,'
                    'sourceip CHAR(30) NOT NULL,'
                    'summary_info CHAR(50),'
                    'logindate timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP')
#用户操作审计表
auditInfoTable = ('audit_info',
                  'username CHAR(30) NOT NULL,'
                  'sourceip CHAR(30) NOT NULL,'
                  'ops VARCHAR(255) NOT NULL,'
                  'opstime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,'
                  'retcode INT(4)'
                  )

devlistTable = ('devlist',
                'id INT(11) NOT NULL primary key AUTO_INCREMENT,'
                'name CHAR(30) NOT NULL,'
                'asset_number CHAR(30) NOT NULL,'
                'owner CHAR(30) NOT NULL,'
                'being_user CHAR(30),'
                'ip_address CHAR(30),'
                'console_info CHAR(30),'
                'if_online CHAR(1) DEFAULT "n",'
                'note text'
                )

def create_tables(tablesList):
    db = connect_db()
    dbCursor = db.cursor()
    for t in tablesList:
        try:
            dbCursor.execute("DROP TABLE IF EXISTS %s"%t[0])
            print "DROP TABLE IF EXISTS %s;"%t[0]
            db.commit()
            createTableSql = "CREATE TABLE IF NOT EXISTS %s (%s)"%(t[0], t[1])
            #try:
            dbCursor.execute(createTableSql)
            #except MySQLdb.Error, e:
                #print '%s\r\n%s'%(e, createTableSql)
            db.commit()
        except Exception, e:
            print 'error:   ',t[0]
            print e
    db.close()
    
if __name__ == '__main__':
    #格式： 表 = ('表名','表结构')
    tablesList = []
    tablesList.extend([ devlistTable,
                        userInfoTable,
                        loginRecordTable,
                        auditInfoTable])
    #创建表
    create_tables(tablesList)

 


