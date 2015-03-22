# -*- coding: utf-8 -*-
#@date  :2015-3-22

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import tornado.gen
import os
import check
from mod import get

from tornado.options import define, options
define('port', default=80, help='run on the given port', type=int)

class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r'/',WechatHandler)
            ]
        settings = dict(
            cookie_secret="7CA71A57B571B5AEAC5E64C6042415DE",
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            debug=True
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class WechatHandler(tornado.web.RequestHandler):

    @property
    def unitsmap(self):
        return {
            'rules':self.rules,
            'lists':self.lists,
            'vote':self.vote,
            'nothing':self.nothing
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
                    self.write(self.wx.response_text_msg('welcome'))
                    self.finish()
                elif self.wx.event == 'unsubscribe':
                    self.write(self.wx.response_text_msg('welcome next'))
                    self.finish()
                elif self.wx.event == 'CLICK':
                    try:
                        self.unitsmap[self.wx.event_key]
                    except KeyError:
                        pass
                    self.finish()
            elif self.wx.msg_type == 'text':
                self.unitsmap[self.wx.content]
                self.finish()

            else:
                self.write(self.wx.response_text_msg(u'??'))
                self.finish()
        else:
            self.write('message processing fail')
            self.finish()
               
    def rules(self):
        msg = get.rules()
        self.write(self.wx.response_text_msg(msg))
    def lists(self):
        msg = get.lists()
        self.write(self.wx.response_text_msg(msg))
    def vote(self):
        msg = get.vote()
        self.write(self.wx.response_text_msg(msg))
    def nothing(self):
        msg = u'无法识别的命令T_T'
        self.write(self.wx.response_text_msg(msg))


if __name__ == '__main__':
    tornado.options.parse_command_line()
    Application().listen(options.port)
    tornado.ioloop.IOLoop.instance().start()