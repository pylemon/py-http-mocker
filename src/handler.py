# -*- coding: utf-8 -*-
import json
import logging as log
import os

import tornado.web

JSON_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../json/')


class BaseHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def prepare(self):
        method = self.request.method
        if method in ("POST", "DELETE"):
            data = json.dumps(json.loads(self.request.body), indent=2)
        else:
            data = self.request.query

        log.info("[{}]{}://{}{}\n{}\n".format(
            method, self.request.protocol, self.request.host, self.request.path, data))

        file_path = "{}{}{}.json".format(JSON_DIR, method.lower(), self.request.path.replace('/', '.'))
        if not os.path.exists(file_path):
            file_path = ""
        else:
            with open(file_path) as f:
                data = json.loads(f.read())
                self.write_200(data)

        if not file_path:
            self.write({'error': 'json file not found'})
            self.write_error(404)

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


class MainHandler(BaseHandler):
    def get(self, path):
        pass

    def post(self, path):
        pass

    def put(self, path):
        pass

    def delete(self, path):
        pass
