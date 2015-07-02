# -*- coding: utf-8 -*-
from tornado.httpclient import HTTPRequest, AsyncHTTPClient,HTTPClient
import tornado.web
import tornado.gen
import urllib, re
import json
from teacher import Teacher
from config import *

class UpdateHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def get(self,openid):
        # self.write(openid)
        # self.finish()
        self.render('update.html',openid = openid)
    @tornado.web.asynchronous
    # @tornado.gen.engine
    def post(self,openid):
        old_password = self.get_argument('old_password',default = None)
        new_password = self.get_argument('new_password',default = None)
        repeat_password = self.get_argument('repeat_password',default = None)
        print openid
        flag = True
        if not openid:
            self.write('access failed')
            self.finish()
            flag = False
            return
        elif len(new_password)<6:
            self.write('新密码至少6位哦')
            self.finish()
            flag = False
            return
        elif new_password!=repeat_password:
            self.write('两次密码不一致')
            self.finish()
            flag = False
            return
        if flag:
            newUser = False
            try:
                teacher = self.db.query(Teacher).filter(Teacher.openid == openid).one()
                if(teacher.password != old_password):
                    self.write('原密码错误')
                    self.finish()
                else:
                    teacher.password = new_password
                    self.db.add(teacher)
                    self.db.commit()
                    self.write('success')
                    self.finish()
                    self.db.close()
            except:
                newUser = True
                self.write('尚未进行绑定')
                self.finish()
            
    