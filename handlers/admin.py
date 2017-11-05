#!/usr/bin/env python
# -*- coding: utf-8 -*-
from db.dbMysql import * 
import datetime
import json
import tornado
import time

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class AdminIndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        if self.get_current_user() == 'admin':
            self.render('adminindex.html')

class AddDevHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        pass


handlers = [(r"/admin", AdminIndexHandler),
            (r"/admin/dev", AddDevHandler)]
