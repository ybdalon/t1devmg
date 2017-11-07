#!/usr/bin/env python
# -*- coding: utf-8 -*-
from db.dbMysql import * 
import datetime
import json
import tornado
import time
import urllib

def convert_querylist_to_json(rows):
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
    return {"status": "200", "message": "ok", "data": json_data}

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
            self.write(convert_querylist_to_json(rows))

    @tornado.web.authenticated
    def post(self, action):
        if self.get_current_user() != "admin":
            'forbidden return error'
            return
        recv_json = json.JSONDecoder().decode(urllib.unquote(self.request.body))
        name = recv_json['name']
        devtype = recv_json['devtype']
        asset_number = recv_json['asset_number']
        owner = recv_json['owner']
        being_user = recv_json['being_user']
        ip_address = recv_json['ip_address']
        console_info = recv_json['console_info']
        note = recv_json['note']
        dbconn = my_db.get_one_conn()
        dbCursor = dbconn.cursor()


        if action == 'add':
            dbCursor.execute( 'INSERT INTO devlist (name, devtype, asset_number, owner, being_user, ip_address, console_info, note) VALUES ' \
            '(%s, %s, %s, %s, %s, %s, %s, %s)', [name, devtype, asset_number, owner, being_user, ip_address, console_info, note])
            dbconn.commit()
        elif action == 'del':
            dbCursor.execute('DELETE FROM devlist WHERE asset_number=%s AND owner=%s', [asset_number, owner])
            dbconn.commit()
        elif action == 'mod':
            dbCursor.execute('UPDATE devlist SET name=%s, devtype=%s, owner=%s, being_user=%s, ip_address=%s, console_info=%s, note=%s' \
            'WHERE asset_number=%s', [name, devtype, owner, being_user, ip_address, console_info, note, asset_number])
            dbconn.commit()

handlers = [(r"/admin", AdminIndexHandler),
            (r"/admin/dev/(\w+)", DevMgHandler)]
