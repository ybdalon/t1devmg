#!/usr/bin/env python
# -*- coding: utf-8 -*-
##################################################################
#一定注意： 现在没有对插入或者更新数据库的字段做判断
#
##################################################################

from db.dbMysql import *
import datetime, os
import json
import tornado
from tornado.web import RequestHandler, HTTPError
import urllib

result_info = {'unknow_error':{'result':'4', 'reason':'unknow error'},
               'wrong_username':{'result':'3', 'reason':'username or password wrong'},
               'wrong_passwd':{'result':'2', 'reason':' username or password wrong'},
               'error_content':{'result':'1', 'reason':'wrong post content'},
               'do_success':{'result':'0', 'reason':'success'},
               'down_addr':{'result':'10', 'reason':'address_json is not match'}
               }

import copy
#检查用户名是否正确
def check_passwd(dbCursor, username, passwd):
    dbCursor.execute('SELECT passwd FROM users WHERE name=%s', [username, ])
    row = dbCursor.fetchone()
    if not row:
        'code:3 ERROR: username is not exist!'
        rescode = result_info['wrong_username'].deepcopy()
    elif row[0] != passwd:
        'code:2 ERROR: passwd is wrong!'
        rescode = result_info['wrong_passwd'].copy()
    elif row[0] == passwd:
        'code:0 INFO: successful '
        rescode = copy.deepcopy(result_info['do_success'])
    else:
        'code:1 INFO: unknow error!'
        rescode = result_info['unknow_error'].copy()
    return rescode


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class indexHandler(BaseHandler):
    def get(self):
    # 判断 current_user, 如果不存在值,进入login页面，否则进入管理界面
        if not self.current_user:
            self.render('login.html')
        elif self.current_user == 'admin':
            self.redirect('/admin')
        else:
            self.redirect('/user')

class LoginHandler(BaseHandler):
    def post(self):
        username = self.get_argument('username')
        passwd = self.get_argument('password')
        dbcon = my_db.get_one_conn()
        dbCursor = dbcon.cursor()
        checkRes = check_passwd(dbCursor, username, passwd)
        if checkRes['result'] == '0':
            self.set_secure_cookie("user", username)
            dbCursor.execute('INSERT INTO login_record '
                             '(username, sourceip, summary_info) '
                             'VALUES (%s, %s, %s)', [username, self.request.remote_ip, 'app login success'])
            dbcon.commit()
            if username == 'admin':
                self.redirect('/admin')
            else:
                self.redirect('/user')
        else:
            self.render("login.html")
        dbCursor.close()

class LogoutHandler(BaseHandler):
    def get(self):
        if self.current_user:
            self.clear_cookie("user")
            self.redirect("/login.html")
        dbCon = dbMysql.my_db.get_one_conn()
        dbCursor = dbCon.cursor()
        dbCursor.execute('delete from online_users_info where username=%s', [name])
        dbCon.commit()
        dbCursor.close()


handlers = [(r"/", indexHandler),
            (r"/login", LoginHandler),
            (r"/logout", LogoutHandler),
           ]






