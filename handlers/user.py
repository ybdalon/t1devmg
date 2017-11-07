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

class UserIndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('user.html')

class UserDevHandler(BaseHandler):
    def get(self, action):
        if action =='list':
            scope = self.get_argument('scope')
            username = self.get_current_user()
            dbcon = my_db.get_one_conn()
            dbCursor = dbcon.cursor()
            if not scope:
                'return error'
                dbCursor.close()
            elif scope == 'all':
                dbCursor.execute('SELECT * FROM devlist')
                rows = dbCursor.fetchall()
                self.write(convert_querylist_to_json(rows))

            elif scope == 'my':
                dbCursor.execute('SELECT * FROM devlist WHERE owner=%s', [username])
                rows = dbCursor.fetchall()
                self.write(convert_querylist_to_json(rows))

            elif scope == 'borrow':
                username = self.get_current_user()
                dbCursor.execute('SELECT * FROM devlist WHERE owner!=%s and being_user=%s', [username, username])
                rows = dbCursor.fetchall()
                self.write(convert_querylist_to_json(rows))

            elif scope == 'lend':
                username = self.get_current_user()
                dbCursor.execute('SELECT * FROM devlist WHERE owner==%s and being_user!=%s', [username, username])
                rows = dbCursor.fetchall()
                self.write(convert_querylist_to_json(rows))

    @tornado.web.authenticated
    def post(self, action):
        username = self.get_current_user()
        recv_json = json.JSONDecoder().decode(urllib.unquote(self.request.body))
        name = recv_json['name']
        devtype = recv_json['devtype']
        asset_number = recv_json['asset_number']
        owner = recv_json['owner']
        being_user = recv_json['being_user']
        ip_address = recv_json['ip_address']
        console_info = recv_json['console_info']
        note = recv_json['note']
        dbCon = my_db.get_one_conn()
        dbCursor = dbCon.cursor()
        if owner != username:
            if action == 'add':
                dbCursor.execute('INSERT INTO devlist (name, devtype, asset_number, owner, being_user, ip_address, console_info, note) VALUES ' \
                '(%s, %s, %s, %s, %s, %s, %s, %s)', [name, devtype, asset_number, owner, being_user, ip_address, console_info, note])
                dbCon.commit()
            elif action == 'del':
                dbCursor.execute('DELETE FROM devlist WHERE asset_number=%s AND owner=%s', [asset_number, owner])
                dbCon.commit()
            elif action == 'mod':
                dbCursor.excute('UPDATE devlist SET name=%s, devtype=%s, owner=%s, being_user=%s, ip_address=%s, console_info=%s, note=%s' \
                'WHERE asset_number=%s', [name, devtype, owner, being_user, ip_address, console_info, note, asset_number])
                dbCon.commit()
        else:
            'forbiden'


handlers = [(r"/user", UserIndexHandler),
            (r"/user/dev/(\w+)", UserDevHandler)]
