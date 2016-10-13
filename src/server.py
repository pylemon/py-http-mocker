# -*- coding: utf-8 -*-
import sys

import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options

from handler import MainHandler

reload(sys)
sys.setdefaultencoding('utf-8')

define("port", default=5000, help="Run server on a specific port", type=int)

settings = {
    "debug": True,
    "logging": "debug",
    "log_to_stderr": True,
}


def get_application():
    return tornado.web.Application([
        (r"/(.*)", MainHandler),
    ], **settings)


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(get_application())
    options.parse_command_line()
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
