<<<<<<< HEAD
#!/usr/bin/python
# -*- coding: utf-8 -*-
#@date  :2015-3-22

from config import *
from sqlalchemy.orm import scoped_session, sessionmaker
from mod.register import registerHandler
from mod.allweixin import allweixinHandler
from mod.db import engine
from mod.getCon import *
from sqlalchemy.orm.exc import NoResultFound
from mod.user import User
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import tornado.gen
import os, sys
import check
import random
from time import localtime, strftime, time



from tornado.options import define, options
define('port', default=7000, help='run on the given port', type=int)

class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r'/wechata/',WechatHandler),
            (r'/wechata/register/([\S]+)',registerHandler),
            (r'/wechata/allweixin',allweixinHandler),
            ]
        settings = dict(
            cookie_secret="7CA71A57B571B5AEAC5E64C6042415DE",
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            # static_url_prefix = os.path.join(os.path.dirname(__file__), '/images/'),
            debug=True
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = scoped_session(sessionmaker(bind=engine,
                                              autocommit=False, autoflush=True,
                                              expire_on_commit=False))


class WechatHandler(tornado.web.RequestHandler):

    @property
    def db(self):
        return self.application.db
    @property
    def unitsmap(self):
        return {
            'nothing':self.nothing,
            'information':self.information,
            'test':self.test,
            'jiang_list':self.jiang_list,
            'jiang_query':self.jiang_query,
            'zhu_query':self.zhu_query,
            'zhu_list':self.zhu_list,
            'ask':self.ask,
            'loan':self.loan,
            'loan2':self.loan2,
            'greenroad':self.greenroad
        }
    def on_finish(self):
        self.db.close()

    def get(self):
        self.wx = check.Message(token='SeuSoft')
        if self.wx.check_signature(self.get_argument('signature', default=''),
                                   self.get_argument('timestamp', default=''),
                                   self.get_argument('nonce', default='')
                                   ):
            self.write(self.get_argument('echostr'))
        else:
            self.write('access verification fail')

    @tornado.web.asynchronous
    def post(self):
        self.wx = check.Message(token='SeuSoft')
        if self.wx.check_signature(self.get_argument('signature', default=''),
                                   self.get_argument('timestamp', default=''),
                                   self.get_argument('nonce', default='')
                                   ):
            self.wx.parse_msg(self.request.body)
            try:
                if self.wx.msg_type == 'event' :
                    if self.wx.event =='subscribe':
                        self.write(self.wx.response_text_msg(ResponseContent))
                        self.finish()
                    elif self.wx.event == 'unsubscribe':
                        self.write(self.wx.response_text_msg(u'谢谢您的关注'))
                        self.finish()
                    elif self.wx.event == 'CLICK':
                        try:
                            self.unitsmap[self.wx.event_key]()
                        except KeyError:
                            pass
                        self.finish()
                elif self.wx.msg_type == 'text':
                    self.unitsmap[self.wx.content]()
                    self.finish()

                else:
                    self.write(self.wx.response_text_msg(u'??'))
                    self.finish()
            except:
                with open('wechat_error.log','a+') as f:
                    f.write(strftime('%Y%m%d %H:%M:%S in [wechat]', localtime(time()))+'\n'+str(sys.exc_info()[0])+str(sys.exc_info()[1])+'\n\n')
                self.write(self.wx.response_text_msg(u'出了点问题T_T,稍后再试吧~'))
                self.finish()
        else:
            self.write('message processing fail')
            self.finish()
    
    def nothing(self):
        # msg = u'您好! 您可以直接回复“提问+您的问题”我们将为您解答，答疑时间为周一至周五09：00-17：00. 东南大学学生事务服务中心联系方式：025-52090282，九龙湖校区大活524。'
        msg = u' '
        # self.write(self.wx.response_text_msg(msg))
    def information(self):
        msg = ResponseContent
        self.write(self.wx.response_text_msg(msg))
    def ask(self):
        msg = u'感谢您的提问！工作人员会及时回答您的提问，请耐心等待。'
        self.write(self.wx.response_text_msg(msg))
    def loan(self):
        self.write(self.wx.response_pic_msg(u"【入学指南】之 新生资助政策",loan_pic_url,u'【入学指南】之 新生资助政策',loan_url))
    def loan2(self):
        self.write(self.wx.response_pic_msg(u"【入学指南】之 生源地贷款",loan2_pic_url,u'【入学指南】之 生源地贷款',loan2_url))
    def greenroad(self):
        self.write(self.wx.response_pic_msg(u"【入学指南】之绿色通道如何办理",greenroad_pic_url,u'【入学指南】之绿色通道如何办理',greenroad_url))
    def test(self):
        msg = u'<a href="%s/allweixin">test</a>' %URL
        self.write(self.wx.response_text_msg(msg))
    def jiang_list(self):
        try:
            user = self.db.query(User).filter(User.openid == self.wx.openid).one()
            msg = jiang_list(user)
            self.write(self.wx.response_text_msg(msg))
        except NoResultFound:
            msg = u'<a href="%s/register/%s">您尚未进行绑定，点我进行绑定哦</a>' % (LOCAL, self.wx.openid)
            self.write(self.wx.response_text_msg(msg))
    def jiang_query(self):
        try:
            user = self.db.query(User).filter(User.openid == self.wx.openid).one()
            msg = jiang_query(user)
            self.write(self.wx.response_text_msg(msg))
        except NoResultFound:
            msg = u'<a href="%s/register/%s">您尚未进行绑定，点我进行绑定哦</a>' % (LOCAL, self.wx.openid)
            self.write(self.wx.response_text_msg(msg))
    def zhu_query(self):
        try:
            user = self.db.query(User).filter(User.openid == self.wx.openid).one()
            msg = zhu_query(user)
            self.write(self.wx.response_text_msg(msg))
        except NoResultFound:
            msg = u'<a href="%s/register/%s">您尚未进行绑定，点我进行绑定哦</a>' % (LOCAL, self.wx.openid)
            self.write(self.wx.response_text_msg(msg))
    def zhu_list(self):
        try:
            user = self.db.query(User).filter(User.openid == self.wx.openid).one()
            msg = zhu_list(user)
            self.write(self.wx.response_text_msg(msg))
        except NoResultFound:
            msg = u'<a href="%s/register/%s">您尚未进行绑定，点我进行绑定哦</a>' % (LOCAL, self.wx.openid)
            self.write(self.wx.response_text_msg(msg))

    # def change_pwd(self):
    #     try:
    #         teacher = self.db.query(Teacher).filter(Teacher.openid == self.wx.openid).one()
    #         msg = u'尊敬的%s,您好！<a href="%s/update/%s">点击修改密码</a>' %(teacher.name,URL,self.wx.openid)
    #         self.write(self.wx.response_text_msg(msg))
    #     except NoResultFound:
    #         msg = u'<a href="%s/Tregister/%s">您尚未进行登录注册，点我进行注册登录哦</a>' % (URL, self.wx.openid)
    #         self.write(self.wx.response_text_msg(msg))
    # def delete(self):
    #     try:
    #         teacher = self.db.query(Teacher).filter(Teacher.openid == self.wx.openid).one()
    #         teacher.openid = None
    #         msg = u'尊敬的%s,您好！注销成功' % teacher.name
    #         self.write(self.wx.response_text_msg(msg))
    #     except NoResultFound:
    #         msg = u'<a href="%s/Tregister/%s">您尚未进行登录注册，点我进行注册登录哦</a>' % (URL, self.wx.openid)
    #         self.write(self.wx.response_text_msg(msg))
    # def register_infor(self):
    #     try:
    #         teacher = self.db.query(Teacher).filter(Teacher.openid == self.wx.openid).one()
    #         msg = u'尊敬的%s，您好！您的房间号为:%s' % (teacher.name,teacher.room)
    #         self.write(self.wx.response_text_msg(msg))
    #     except NoResultFound:
    #         msg = u'<a href="%s/Tregister/%s">您尚未进行登录注册，点我进行注册登录哦</a>' % (URL, self.wx.openid)
    #         self.write(self.wx.response_text_msg(msg))
    # def party_arrangement(self):
    #     try:
    #         teacher = self.db.query(Teacher).filter(Teacher.openid == self.wx.openid).one()
    #         msg = u'尊敬的%s，您好！<a href="%s">点击查看详细会议安排</a>' % (teacher.name,party_url)
    #         self.write(self.wx.response_text_msg(msg))
    #     except NoResultFound:
    #         msg = u'<a href="%s/Tregister/%s">您尚未进行登录注册，点我进行注册登录哦</a>' % (URL, self.wx.openid)
    #         self.write(self.wx.response_text_msg(msg))
    # def download(self):
    #     try:
    #         teacher = self.db.query(Teacher).filter(Teacher.openid == self.wx.openid).one()
    #         msg = u'尊敬的%s，您好，<a href="%s/fileList">请点击下载资料</a>' % (teacher.name,URL)
    #         self.write(self.wx.response_text_msg(msg))
    #     except NoResultFound:
    #         msg = u'<a href="%s/Tregister/%s">您尚未进行登录注册，点我进行注册登录哦</a>' % (URL, self.wx.openid)
    #         self.write(self.wx.response_text_msg(msg))
    # def communicate(self):
    #     try:
    #         teacher = self.db.query(Teacher).filter(Teacher.openid == self.wx.openid).one()
    #         msg = u'尊敬的%s，您好，<a href="%s">请点击加入交流群</a>' % (teacher.name,com_url)
    #         self.write(self.wx.response_text_msg(msg))
    #     except NoResultFound:
    #         msg = u'<a href="%s/Tregister/%s">您尚未进行登录注册，点我进行注册登录哦</a>' % (URL, self.wx.openid)
    #         self.write(self.wx.response_text_msg(msg))
    


if __name__ == '__main__':
    tornado.options.parse_command_line()
    Application().listen(options.port)
=======
#!/usr/bin/python
# -*- coding: utf-8 -*-
#@date  :2015-3-22

from config import *
from sqlalchemy.orm import scoped_session, sessionmaker
from mod.register import registerHandler
from mod.allweixin import allweixinHandler
from mod.model.db import engine
from mod.getCon import *
from sqlalchemy.orm.exc import NoResultFound
from mod.model.user import User
from mod.model.wekeyword import WeKeyWord

from mod.keyword import keywordHandler
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import tornado.gen
import os, sys
import check
import random
from time import localtime, strftime, time
import traceback



from tornado.options import define, options
define('port', default=7000, help='run on the given port', type=int)

class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r'/wechata/',WechatHandler),
            (r'/wechata/register/([\S]+)',registerHandler),
            (r'/wechata/allweixin',allweixinHandler),
            (r'/wechata/keyword',keywordHandler)
            ]
        settings = dict(
            cookie_secret="7CA71A57B571B5AEAC5E64C6042415DE",
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            debug=True
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = scoped_session(sessionmaker(bind=engine,
                                              autocommit=False, autoflush=True,
                                              expire_on_commit=False))


class WechatHandler(tornado.web.RequestHandler):

    @property
    def db(self):
        return self.application.db
    @property
    def unitsmap(self):
        return {
            'nothing':self.nothing,
            'information':self.information,
            'jiang_list':self.jiang_list,
            'jiang_query':self.jiang_query,
            'zhu_query':self.zhu_query,
            'zhu_list':self.zhu_list,
            'ask':self.ask
        }
    def on_finish(self):
        self.db.close()

    def get(self):
        self.wx = check.Message(token='SeuSoft')
        if self.wx.check_signature(self.get_argument('signature', default=''),
                                   self.get_argument('timestamp', default=''),
                                   self.get_argument('nonce', default='')
                                   ):
            self.write(self.get_argument('echostr'))
        else:
            self.write('access verification fail')

    @tornado.web.asynchronous
    def post(self):
        self.wx = check.Message(token='SeuSoft')
        if self.wx.check_signature(self.get_argument('signature', default=''),
                                   self.get_argument('timestamp', default=''),
                                   self.get_argument('nonce', default='')
                                   ):
            self.wx.parse_msg(self.request.body)
            try:
                if self.wx.msg_type == 'event' :
                    if self.wx.event =='subscribe':
                        self.write(self.wx.response_text_msg(ResponseContent))
                        self.finish()
                    elif self.wx.event == 'unsubscribe':
                        self.write(self.wx.response_text_msg(u'谢谢您的关注'))
                        self.finish()
                    elif self.wx.event == 'CLICK':
                        try:
                            self.unitsmap[self.wx.event_key]()
                        except KeyError:
                            pass
                        self.finish()
                elif self.wx.msg_type == 'text':
                    key = self.wx.content_key(self.wx.content)
                    if key == 'nothing':
                        self.nothing(self.wx.content)
                    else:
                        self.unitsmap[key]()
                    self.finish()
                elif self.wx.msg_type == 'voice':
                    key = self.wx.content_key(self.wx.voice_content)
                    if key == 'nothing':
                        self.nothing(self.wx.self.wx.voice_content)
                    else:
                        self.unitsmap[key]()
                    self.finish()
                else:
                    self.write(self.wx.response_text_msg(u'??'))
                    self.finish()
            except:
                with open('wechat_error.log','a+') as f:
                    f.write(strftime('%Y%m%d %H:%M:%S in [wechat]', localtime(time()))+'\n'+str(sys.exc_info()[0])+str(sys.exc_info()[1])+'\n\n')
                self.write(self.wx.response_text_msg(u'出了点问题T_T,稍后再试吧~'))
                self.finish()
        else:
            self.write('message processing fail')
            self.finish()
    
    def nothing(self,content):
        msg = u'您好! 您可以直接回复“提问+您的问题”我们将为您解答，答疑时间为周一至周五09：00-17：00. 东南大学学生事务服务中心联系方式：025-52090282，九龙湖校区大活524。'
        try:
            keyword = self.db.query(WeKeyWord).all()
            for i in keyword:
                if content in i.keyword:
                    msg = i.response
        except:
            pass
        self.write(self.wx.response_text_msg(msg))
    def information(self):
        msg = ResponseContent
        self.write(self.wx.response_text_msg(msg))
    def ask(self):
        msg = u'感谢您的提问！工作人员会及时回答您的提问，请耐心等待。'
        self.write(self.wx.response_text_msg(msg))
    def jiang_list(self):
        try:
            user = self.db.query(User).filter(User.openid == self.wx.openid).one()
            msg = jiang_list(user)
            self.write(self.wx.response_text_msg(msg))
        except NoResultFound:
            msg = u'<a href="%s/register/%s">您尚未进行绑定，点我进行绑定哦</a>' % (LOCAL, self.wx.openid)
            self.write(self.wx.response_text_msg(msg))
    def jiang_query(self):
        try:
            user = self.db.query(User).filter(User.openid == self.wx.openid).one()
            msg = jiang_query(user)
            self.write(self.wx.response_text_msg(msg))
        except NoResultFound:
            msg = u'<a href="%s/register/%s">您尚未进行绑定，点我进行绑定哦</a>' % (LOCAL, self.wx.openid)
            self.write(self.wx.response_text_msg(msg))
    def zhu_query(self):
        try:
            user = self.db.query(User).filter(User.openid == self.wx.openid).one()
            msg = zhu_query(user)
            self.write(self.wx.response_text_msg(msg))
        except NoResultFound:
            msg = u'<a href="%s/register/%s">您尚未进行绑定，点我进行绑定哦</a>' % (LOCAL, self.wx.openid)
            self.write(self.wx.response_text_msg(msg))
    def zhu_list(self):
        try:
            user = self.db.query(User).filter(User.openid == self.wx.openid).one()
            msg = zhu_list(user)
            self.write(self.wx.response_text_msg(msg))
        except NoResultFound:
            msg = u'<a href="%s/register/%s">您尚未进行绑定，点我进行绑定哦</a>' % (LOCAL, self.wx.openid)
            self.write(self.wx.response_text_msg(msg))
    


if __name__ == '__main__':
    tornado.options.parse_command_line()
    Application().listen(options.port)
>>>>>>> origin/master
    tornado.ioloop.IOLoop.instance().start()