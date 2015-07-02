# -*- coding: utf-8 -*-
from tornado.httpclient import HTTPRequest, AsyncHTTPClient,HTTPClient
import tornado.web
import tornado.gen
import urllib, re
import codecs
import json
from user import User
from config import *
import os
files=['会务手册.docx',u'各高校大学生综合素质评价办法.pdf']
class FileHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def get(self,filename):
        print('i download file handler : ',filename)
        with open('File/'+filename, "rb") as f:
          self.set_header('Content-Type','application/octet-stream')
          self.write(f.read())
        print 'ok'
        self.finish()
            

    @tornado.web.asynchronous
    # @tornado.gen.engine
    def post(self,openid):
        self.write('hello')
        self.finish()

class FileListHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def get(self):
        self.render('fileList.html',files=files)
            

    @tornado.web.asynchronous
    # @tornado.gen.engine
    def post(self,openid):
        self.write('hello')
        self.finish()