<<<<<<< HEAD
#!/usr/bin/python
# -*- coding: utf-8 -*-
import hashlib
import time
import xml.etree.ElementTree as ET

class Message(object):

    TEXT_MSG = u"""
<xml>
<ToUserName><![CDATA[{to_user_name}]]></ToUserName>
<FromUserName><![CDATA[{from_user_name}]]></FromUserName>
<CreateTime>{create_time}</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[{content}]]></Content>
</xml>
"""
    def __init__(self, token):
        self.token = token
        self.msg = {}

        
    def check_signature(self, signature, timestamp, nonce):
        tmplist = [self.token, timestamp, nonce]
        tmplist.sort()
        tmpstr = ''.join(tmplist)
        hashstr = hashlib.sha1(tmpstr).hexdigest()

        if hashstr == signature:
            return True
        else:
            return False

    def parse_msg(self, msg):
        root = ET.fromstring(msg)
        for child in root:
            self.msg[child.tag] = child.text
        return self.msg

    @property
    def msg_type(self):
        return self.msg.get('MsgType', None)

    @property
    def event(self):
        return self.msg.get('Event', None)

    @property
    def event_key(self):
        return self.msg.get('EventKey', None)

    @property
    def raw_content(self):
        return self.msg.get('Content', None)

    @property
    def content(self):
        content = self.msg.get('Content',None)
        if u'提问' in content:
            return 'ask'
        elif content==u'勤工助学' or content==u'资助育人活动' or content==u'其他' :
            return 'information'
        elif content == u'test':
            return 'test'
        elif content == u'j':
            return 'jiang_list'
        elif content == u'q':
            return 'jiang_query'
        elif content == u't':
            return 'zhu_query'
        else:
            return 'nothing'
    @property
    def openid(self):
        return self.msg.get('FromUserName', None)
    def response_text_msg(self, content):
        return self.TEXT_MSG.format(to_user_name=self.msg['FromUserName'],
                                    from_user_name=self.msg['ToUserName'],
                                    create_time=str(int(time.time())),
                                    content=content)

    def response_pic_msg(self, title, pic_url, content, url):
        return self.PIC_MSG.format(to_user_name=self.msg['FromUserName'],
                                    from_user_name=self.msg['ToUserName'],
                                    create_time=str(int(time.time())),
                                    title=title,
                                    description=content,
                                    picurl=pic_url,
                                    url=url)
=======
#!/usr/bin/python
# -*- coding: utf-8 -*-
import hashlib
import time
import xml.etree.ElementTree as ET

class Message(object):

    TEXT_MSG = u"""
<xml>
<ToUserName><![CDATA[{to_user_name}]]></ToUserName>
<FromUserName><![CDATA[{from_user_name}]]></FromUserName>
<CreateTime>{create_time}</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[{content}]]></Content>
</xml>
"""
    def __init__(self, token):
        self.token = token
        self.msg = {}

        
    def check_signature(self, signature, timestamp, nonce):
        tmplist = [self.token, timestamp, nonce]
        tmplist.sort()
        tmpstr = ''.join(tmplist)
        hashstr = hashlib.sha1(tmpstr).hexdigest()

        if hashstr == signature:
            return True
        else:
            return False

    def parse_msg(self, msg):
        root = ET.fromstring(msg)
        for child in root:
            print child.tag,child.text
            self.msg[child.tag] = child.text
        return self.msg

    @property
    def msg_type(self):
        return self.msg.get('MsgType', None)

    @property
    def event(self):
        return self.msg.get('Event', None)

    @property
    def voice_content(self):
        return self.msg.get('Recognition',None)


    @property
    def event_key(self):
        return self.msg.get('EventKey', None)

    @property
    def raw_content(self):
        return self.msg.get('Content', None)

    def content_key(self,content):
        if content:
            if u'提问' in content:
                return 'ask'
            elif content==u'勤工助学' or content==u'资助育人活动' or content==u'其他' :
                return 'information'
            elif content == u'test':
                return 'test'
            elif content == u'j':
                return 'jiang_list'
            elif content == u'q':
                return 'jiang_query'
            elif content == u't':
                return 'zhu_query'
            elif content == 'test':
                return 'test'
            else:
                return 'nothing'
        else:
            return 'nothing'
    @property
    def content(self):
        content = self.msg.get('Content',None)
        return content
        
    @property
    def openid(self):
        return self.msg.get('FromUserName', None)
    def response_text_msg(self, content):
        return self.TEXT_MSG.format(to_user_name=self.msg['FromUserName'],
                                    from_user_name=self.msg['ToUserName'],
                                    create_time=str(int(time.time())),
                                    content=content)
>>>>>>> origin/master
