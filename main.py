# -*- coding: utf-8 -*-
#@date  :2015-3-22

from config import *
from sqlalchemy.orm import scoped_session, sessionmaker
from mod.register import registerHandler
from mod.Tregister import TregisterHandler
from mod.update import UpdateHandler
from mod.db import engine
from sqlalchemy.orm.exc import NoResultFound
from mod.user import User
from mod.teacher import Teacher
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import tornado.gen
import os
import check
import random



from tornado.options import define, options
define('port', default=80, help='run on the given port', type=int)

class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r'/',WechatHandler),
            (r'/Tregister/([\S]+)',TregisterHandler),
            (r'/update/([\S]+)',UpdateHandler),
            (r'/register/([\S]+)',registerHandler)
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
            'rules':self.we_rules,
            'lists':self.we_lists,
            'result':self.we_result,
            'nothing':self.nothing,
            'information':self.information,
            'party':self.party_arrangement,
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
        else:
            self.write('message processing fail')
            self.finish()
               
    def we_rules(self):
        msg = u'<a href="%s/mobile_intro">点击查看活动介绍</a>' % LOCAL
        self.write(self.wx.response_text_msg(msg))
    def we_lists(self):
        msg = u'<a href="%s/mobile_candidate_list">点击查看候选人介绍</a>' % LOCAL
        self.write(self.wx.response_text_msg(msg))
    def we_result(self):
        msg = u'<a href="%s/ranking">点击查看结果</a>' % LOCAL
        self.write(self.wx.response_text_msg(msg))
    def nothing(self):
        msg = u'您好! 您可以直接回复“提问+您的问题”我们将为您解答，答疑时间为周一至周五09：00-17：00. 东南大学学生事务服务中心联系方式：025-52090282，九龙湖校区大活524。'
        self.write(self.wx.response_text_msg(msg))
    def information(self):
        msg = ResponseContent
        self.write(self.wx.response_text_msg(msg))
    def party_arrangement(self):
        try:
            teacher = self.db.query(Teacher).filter(Teacher.openid == self.wx.openid).one()
            msg = u'尊敬的%s，您好！会议将在xxx举行，时间为xxx，地点为xxx' % teacher.name
            self.write(self.wx.response_text_msg(msg))
        except NoResultFound:
            msg = u'<a href="%s/Tregister/%s">您尚未进行登录注册，点我进行注册登录哦</a>' % (URL, self.wx.openid)
            self.write(self.wx.response_text_msg(msg))
    def ask(self):
        msg = u'感谢您的提问！工作人员会及时回答您的提问，请耐心等待'
        self.write(self.wx.response_text_msg(msg))


if __name__ == '__main__':
    tornado.options.parse_command_line()
    Application().listen(options.port)
    tornado.ioloop.IOLoop.instance().start()