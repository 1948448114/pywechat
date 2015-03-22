# -*- coding: utf-8 -*-


from tornado.httpclient import HTTPRequest, HTTPClient, HTTPError

def rules(self):
    msg = u'rules'
    return msg


def lists(self):
    msg = u'lists'
    return msg


def vote(self):
    msg = u'<a href="www.baidu.com">欢迎参与投票！'
    return msg
