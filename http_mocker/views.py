# -*- coding: utf-8 -*-
import json
import logging as log
import os

from http_mocker.utils import BaseHandler

JSON_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../json/')


class ResponseHandler(BaseHandler):
    def prepare(self):
        method = self.request.method
        if method in ("POST", "DELETE"):
            try:
                data = json.dumps(json.loads(self.request.body), indent=2)
            except Exception as e:
                log.info('load req data from body failed: {}'.format(e))
                data = self.request.arguments
        else:
            data = self.request.query

        log.info("[{}]->[{}]{}://{}{}\n{}\n".format(
            self.request.remote_ip, method, self.request.protocol, self.request.host, self.request.path, data))

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


class MainHandler(ResponseHandler):
    def get(self, path):
        pass

    def post(self, path):
        pass

    def put(self, path):
        pass

    def delete(self, path):
        pass

    def options(self, path):
        pass

    def head(self, path):
        pass
