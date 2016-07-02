# -*- coding: utf-8 -*-
# LOCAL = u'http://123.57.221.18'

from tornado.httpclient import HTTPRequest, HTTPClient, HTTPError
from model.user import User
from get_api_return import get_api_return

def jiang_list(user):
    ret = get_api_return('jiang_list',user)
    msg = u''
    if ret['code'] == 200:
        content = ret['content']
        msg += u'可申请奖学金:\n'
        for item in content:
            # msg += u'> %s <a href="%s/jiang_apply/%s">申请</a>\n' % (item['name'],LOCAL,item['id'])
            msg += u'>  %s\n' % item['name']
            msg += u'  开始时间：%s\n' % item['start_time']
            msg += u'  结束时间：%s\n' % item['end_time']
        if not content:
            return u'暂时没有奖学金可申请'
        return msg
    elif ret['code'] == 599:
        return u"正在获取最新数据，再点一次就有啦！"
    else:
        return ret['content']
# 已获得奖学金
def jiang_query(user):
    ret = get_api_return('jiang_query',user)
    msg = u''
    if ret['code'] == 200:
        content = ret['content']
        content_apply = ret['content_apply']
        msg += u'已申请奖学金:\n'
        for item in content:
            msg += u'>  %s\n' % item['name']
            msg += u'学期:%s\n' % item['term']
            mag += u'金额:%s\n' % item['money']
            msg += u'状态:%s\n' % item['state']
        if not content:
            msg += u'没有申请奖学金T_T\n'
        return msg
    elif ret['code'] == 599:
        return u"正在获取最新数据，再点一次就有啦！"
    else:
        return ret['content']
def zhu_query(user):
    ret = get_api_return('zhu_query',user)
    msg = u''
    if ret['code'] == 200:
        content_get = ret['content_get']
        content_apply = ret['content_apply']
        msg += u'正在申请助学金:\n'
        for item in content_apply:
            msg += u'>  %s\n' % item['name']
            msg += u'申请日期:%s\n' % item['apply_time']
            msg += u'状态:%s\n' % item['state']
        if not content_get:
            msg += u'没有申请助学金T_T\n'
        msg += u'\n'
        msg += u'已获得助学金:\n'
        for item in content_get:
            msg += u'>  %s\n' % item['name']
            msg += u'学期:%s\n' % item['apply_time']
            msg += u'金额:%s\n' % item['money']
        if not content_get:
            msg += u'没有获得助学金T_T\n'
        return msg
    elif ret['code'] == 599:
        return u"正在获取最新数据，再点一次就有啦！"
    else:
        return ret['content']

def zhu_list(user):
    ret = get_api_return('zhu_list',user)
    msg = u''
    if ret['code'] == 200:
        content = ret['content']
        msg += u'可申请助学金:\n'
        for item in content:
            # msg += u'> %s <a href="%s/jiang_apply/%s">申请</a>\n' % (item['name'],LOCAL,item['id'])
            msg += u'>  %s\n' % item['name']
            msg += u'创建时间：%s\n' % item['create_time']
            msg += u'发放周期: %s\n' % item['fafangzhouqi']
            msg += u'评定周期: %s\n' % item['pingdingzhouqi']
            msg += u'是否有校外审：%s\n' % item['is_xiaowaishen']
            msg += u'是否基金会助学金:%s\n' % item['is_jijinhui']
        if not content:
            return u'暂时没有助学金可申请'
        return msg
    elif ret['code'] == 599:
        return u"正在获取最新数据，再点一次就有啦！"
    else:
        return ret['content']



