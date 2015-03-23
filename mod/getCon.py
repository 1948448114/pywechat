# -*- coding: utf-8 -*-
LOCAL = u'http://123.57.221.18'

from tornado.httpclient import HTTPRequest, HTTPClient, HTTPError

def rules():
    msg = u'<a href="%s/rules">点击查看规则</a>' % LOCAL
    return msg


def lists():
    msg = u'lists'
    return msg


def vote():
    msg = u'<a href="www.baidu.com">欢迎参与投票！</a>'
    return msg
