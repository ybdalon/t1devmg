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

class UserIndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('user.html')

handlers = [(r"/user", UserIndexHandler)]
