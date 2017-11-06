#!/usr/bin/env python
# -*- coding: utf-8 -*-
from db.dbMysql import *
import datetime
import json
import tornado
from tornado.web import RequestHandler, HTTPError
import time


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class ShowDevList(BaseHandler):
    def get(self):
        db = my_db.get_one_conn()
        dbCursor = db.cursor()
        dbCursor.execute('SELECT * FROM devlist')
        rows = dbCursor.fetchall()
        json_data = []
        for l in rows:
            result = {}
            result['id'] = l[0]
            result['name'] = l[1]
            result['devtype'] = l[2]
            result['asset_number'] = l[3]
            result['owner'] = l[4]
            result['being_user'] = l[5]
            result['ip'] = l[6]
            result['console_info'] = l[7]
            result['if_online'] = l[8]
            result['note'] = l[9]
            json_data.append(result)
        resjson = {"status": "200", "message":"ok", "data": json_data}
        #jsondatar=json.dumps(json_data,ensure_ascii=False)
        self.write(resjson)

    def post(self):
        pass

handlers =  [(r'/devlist', ShowDevList)]
