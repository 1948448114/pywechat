# -*- coding: utf-8 -*-
from tornado.httpclient import HTTPRequest, AsyncHTTPClient,HTTPClient
import tornado.web
import tornado.gen
import urllib, re
import json
from teacher import Teacher
from config import *

class TregisterHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def get(self,openid):
        # self.write(openid)
        # self.finish()
    # @tornado.gen.engine
        self.render('Tregister.html',openid = openid)
    @tornado.web.asynchronous
    def post(self,openid):
        name = self.get_argument('name',default = None)
        password = self.get_argument('password',default = None)
        school = self.get_argument('school',default = None)
        flag = True
        if not openid:
            self.write('access failed')
            self.finish()
            flag = False
            return
        elif not name or not password:
            self.write('请填写完整信息哦')
            self.finish()
            flag = False
            return
        if flag:
            newUser = False
            try:
                teacher = self.db.query(Teacher).filter(Teacher.name == name).one()
                if teacher.openid:
                    self.write('该用户已注册')
                    self.finish()
                elif teacher.password != password:
                    self.write('密码错误')
                    self.finish()
                elif teacher.school != school:
                    self.write('学校信息不正确')
                    self.finish()
                else:
                    teacher.openid = openid
                    teacher.state = 1
                    self.db.add(teacher)
                    self.db.commit()
                    self.write('success')
                    self.finish()
                    self.db.close()
            except:
                newUser = True
                self.write('该用户不存在')
                self.finish()
            
    