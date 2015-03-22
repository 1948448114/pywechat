# -*- coding: utf-8 -*-

import tornado.web


class RuleHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('rule.html')
