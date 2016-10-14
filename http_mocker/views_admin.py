# -*- coding: utf-8 -*-

import runtime
from http_mocker.models import Response
from http_mocker.utils import BaseHandler


class AdminHandler(BaseHandler):
    def get(self):
        with runtime.session_scope() as session:
            response = session.query(Response).all()
            result = []
            for resp in response:
                result.append({
                    'id': resp.id,
                    'name': resp.name,
                    'path': resp.path,
                    'response': resp.response,
                })

        self.write_200({"data": result})

    def post(self, path):
        pass
