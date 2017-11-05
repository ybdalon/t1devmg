#!/usr/bin/env python
# -*- coding: utf-8 -*-
from db.dbMysql import * 
import datetime
import json
import tornado
import time
import urllib

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class AdminIndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        if self.get_current_user() == 'admin':
            self.render('adminindex.html')

class DevMgHandler(BaseHandler):
    def get(self, action):
        if action =='list':
            username = self.get_current_user()
            dbcon = my_db.get_one_conn()
            dbCursor = dbcon.cursor()
            dbCursor.execute('SELECT * FROM devlist')
            rows = dbCursor.fetchall()
            json_data = []
            for l in rows:
                result = {}
                result['id'] = l[0]
                result['dut_type'] = l[1]
                result['asset_number'] = l[2]
                result['owner'] = l[3]
                result['being_user'] = l[4]
                result['ip'] = l[5]
                result['console_info'] = l[6]
                result['if_online'] = l[7]
                result['note'] = l[8]
                json_data.append(result)
            resjson = {"status": "200", "message": "ok", "data": json_data}
            # jsondatar=json.dumps(json_data,ensure_ascii=False)
            self.write(resjson)

    @tornado.web.authenticated
    def post(self, action):
        if self.get_current_user() != "admin":
            'forbidden return error'
            return
        recv_json = json.JSONDecoder().decode(urllib.unquote(self.request.body))
        name = recv_json['name']
        asset_number = recv_json['asset_number']
        owner = recv_json['owner']
        being_user = recv_json['being_user']
        ip_address = recv_json['ip_address']
        console_info = recv_json['console_info']
        note = recv_json['note']
        if action == 'add':
            'INSERT INTO devlist (name, asset_number, owner, being_user, ip_address, console_info, note) VALUES ' \
            '("%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (
            name, asset_number, owner, being_user, ip_address, console_info, note)
        elif action == 'del':
            'DELETE FROM devlist WHERE asset_number="%s" and owner="%s"' % (asset_number, owner)
        elif action == 'mod':
            'UPDATA devlist set name="%s", owner="%s", being_user="%s", ip_address="%s", console_info="%s", note="%s"' \
            'WHERE asset_number="%s" ' % (name, owner, being_user, ip_address, console_info, note, asset_number)



handlers = [(r"/admin", AdminIndexHandler),
            (r"/admin/dev/(\w+)", DevMgHandler)]
