#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import tornado
from tornado import web
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.options import options
import db.dbMysql as db


class Application(web.Application):
    def __init__(self):
        from urls import handlers, sub_handlers#, ui_modules
        settings = dict(
            #debug=options.debug,
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies = False,
            cookie_secret = "81oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            login_url = "/login",
            )
        super(Application, self).__init__(handlers, **settings)

        # add handlers for sub domains
        for sub_handler in sub_handlers:
            # host pattern and handlers
            self.add_handlers(sub_handler[0], sub_handler[1])


def main():
    #tornado.options.parse_command_line()
    http_server = HTTPServer(Application(), xheaders=True)
    port = 8000
    num_processes = 1

    #if options.debug:
    #        num_processes = 1

    #if options.chat_app:
    #        port = port + 1
    #        num_processes = 1
    http_server.bind(int(port))
    http_server.start(int(num_processes))
    IOLoop.instance().start()
    

if __name__ == "__main__":
    main()