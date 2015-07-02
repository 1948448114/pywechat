# -*- coding: utf-8 -*-
from tornado.httpclient import HTTPRequest, AsyncHTTPClient,HTTPClient
import tornado.web
import tornado.gen
import urllib, re
import json


class allweixinHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('allweixin.html')
    @tornado.web.asynchronous
    def post(self):
        self.write('hello')
        self.finish()