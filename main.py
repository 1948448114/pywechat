# -*- coding: utf-8 -*-
#@date  :2015-3-22

from config import LOCAL,ResponseContent
from sqlalchemy.orm import scoped_session, sessionmaker
from mod.register import registerHandler
from mod.db import engine
from mod.user import User
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
            'ask':self.ask
        }

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
                    self.write(self.wx.response_text_msg('谢谢您的关注'))
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
    def ask(self):
        msg = u'感谢您的提问！工作人员会及时回答您的提问，请耐心等待'
        self.write(self.wx.response_text_msg(msg))


if __name__ == '__main__':
    tornado.options.parse_command_line()
    Application().listen(options.port)
    tornado.ioloop.IOLoop.instance().start()