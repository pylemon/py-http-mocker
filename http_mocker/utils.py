# -*- coding: utf-8 -*-
import tornado.web


class FailedOperation(Exception):
    def __init__(self, message, code=None, params=None, key=None, extra_data=None):
        self.code = code
        self.params = params
        self.message = message
        self.key = key
        self.extra_data = repr(extra_data) if extra_data is not None else None

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return "{'code': %s, 'params': %s, 'message': %s, 'i18n_key': %s}" % (
            self.code, self.params, self.message, self.key)


class BaseHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def write_200(self, data):
        self.set_status(200)
        self.add_headers()
        self.write(data)
        self.finish()

    def options(self, *args, **kwargs):
        self.add_headers()

    def add_headers(self):
        self.add_header("Access-Control-Allow-Origin", "*")
        self.add_header("Access-Control-Allow-Methods", "GET,POST,PUT,DELETE,OPTIONS")
        self.add_header("Access-Control-Allow-Credentials", "true")
