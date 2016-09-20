#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.httpclient import HTTPRequest, HTTPClient, HTTPError
from config import *
from time import time, localtime, strftime
import urllib, json
import sys

error_map = {
        599 : u'暂时无法连接，不如待会再试试',        # time out
        408 : u'暂时无法连接，不如待会再试试',        # returned time out
        400 : u'后台接口错误',         # params error
        401 : u'<a href="%s/register/%s">你不是把一卡通密码输错了吧，快点我修改。</a>',                     
                                                     # uuid error
        500 : u'出了点故障，不如待会再试试吧',        # server error
    }

def get_api_return(api_name, user, data={}, timeout=TIME_OUT):
    ret = {}
    client = HTTPClient()
    data['number'] = user.number
    data['password'] = user.password
    params = urllib.urlencode(data)
    request = HTTPRequest(URL + api_name, method='POST',
                          body=params, request_timeout=timeout)
    try:
        response = client.fetch(request)
        ret = json.loads(response.body)
        if 200<=ret['code']< 300:
            return ret
        elif ret['code'] == 401:
            ret['content'] = error_map[401] % (LOCAL, user.openid)
        else:
            ret['content'] = error_map[ret['code']]
    except HTTPError as e:
        ret['code'] = e.code
        if ret['code'] == 401:
            ret['content'] = error_map[401] % (LOCAL, user.openid)
        else:
            ret['content'] = error_map[ret['code']]
    except:
        with open('api_error.log','a+') as f:
            f.write(strftime('%Y%m%d %H:%M:%S in [get_api_return]', localtime(time()))+'\n'+str(sys.exc_info())+'\n['+api_name+']\t'+str(user.number)+'\nString:'+str(ret)+'\n\n')
        ret['code'] = 500
        ret['content'] = u' 服务器未能及时回应请求，不如再试试'
    return ret

