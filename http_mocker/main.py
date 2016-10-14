# -*- coding: utf-8 -*-
import sys

import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options

from http_mocker.views_admin import AdminHandler
from views import MainHandler

reload(sys)
sys.setdefaultencoding('utf-8')

define("port", default=5000, help="Run server on a specific port", type=int)
define("admin_port", default=5001, help="Run admin server on a specific port", type=int)

settings = {
    "debug": True,
    "logging": "debug",
    "log_to_stderr": True,
}


def get_application():
    return tornado.web.Application([
        (r"/(.*)", MainHandler),
    ], **settings)


def get_admin_application():
    return tornado.web.Application([
        (r"/", AdminHandler),
    ], **settings)

if __name__ == "__main__":
    options.parse_command_line()

    http_server = tornado.httpserver.HTTPServer(get_application())
    http_server.listen(options.port)

    admin_http_server = tornado.httpserver.HTTPServer(get_admin_application())
    admin_http_server.listen(options.admin_port)

    tornado.ioloop.IOLoop.instance().start()
