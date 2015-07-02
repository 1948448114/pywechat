# -*- coding: utf-8 -*-
from tornado.httpclient import HTTPRequest, AsyncHTTPClient,HTTPClient
import tornado.web
import tornado.gen
import urllib, re
import json
from user import User
from config import *

class registerHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def get(self,openid):
        # self.write(openid)
        # self.finish()
        self.render('register.html',openid = openid)

    @tornado.web.asynchronous
    # @tornado.gen.engine
    def post(self,openid):
        number = self.get_argument('number',default = None)
        password = self.get_argument('password',default = None)
        flag = True
        print 'openid',openid
        if not openid:
            self.write('access failed')
            self.finish()
            flag = False
        elif not number or not password:
            self.write('请填写完整信息哦')
            self.finish()
            flag = False
        if flag:
            newUser = False
            try:
                user = self.db.query(User).filter(User.openid == openid).one()
                data = {
                    'number':number,
                    'password':password
                }
            except:
                data = {
                    'number':number,
                    'password':password
                }
                newUser = True
            finally:
                try:
                    x = urllib.urlencode(data)
                except:
                    self.write('输入了非法字符==')
                    self.finish()
                    return
                print 'number',number
                print 'password',password
                # self.check(number,password)
                status = self.check_user(data)
                if status == 0:
                    if newUser:
                        print 'get'
                        user = User(openid = openid,
                                    number = number,
                                    password = password,
                                    state = 0)
                        self.db.add(user)
                elif status == 1:
                    self.write('网络较慢，等会儿再试吧')
                    self.finish()
                    self.db.close()
                    return
                elif status == 2:
                    self.write('一卡通或统一身份密码不正确，要不再试一次')
                    self.finish()
                    self.db.close()
                    return
                elif status == 3:
                    self.write('系统故障')
                    self.finish()
                    self.db.close()
                    return
                else:
                    self.write('未知错误')
                    self.finish()
                    self.db.close()
                    return
                self.db.commit()
                self.write('success')
                self.finish()
                self.db.close()
    def check_user(self,data):
        client = HTTPClient()
        request = HTTPRequest(URL+'/checkPWD',method = 'POST',
                              body = urllib.urlencode(data),request_timeout=7)
        try:
            response = client.fetch(request)
            print response.body
            ret = json.loads(response.body)
            # ret = self.check(data['number'],data['password'])
            print ret
            if ret['code'] == 200:
                return 0
            elif ret['code'] == 400:
                return 2
            elif ret['code'] == 408:
                return 1
            elif ret['code'] == 500:
                return 3
            else:
                return 4
        except Exception,e:
            print e
            return 4
    
      



