# -*- coding: utf-8 -*-
import tornado.web
import tornado.gen
import urllib, re
import json
from model.wekeyword import WeKeyWord

class keywordHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def on_finish(self):
        self.db.close()

    def get(self):
        self.render('keyword.html')

    def post(self):
        option_type = self.get_argument("type",default=None)
        ret = {'code':200,'content':''}
        try:
            if not option_type:
                ret['code'] = 400
                ret['content'] = u'参数缺少'
            else:
                keyword = {
                    'all':self.get_all,
                    'add':self.add_one,
                    'delete':self.delete_one
                }
                ret = keyword[option_type]()
        except Exception,e:
            ret['code'] = 500
            ret['contene'] = str(e)

        self.write(json.dumps(ret, ensure_ascii=False, indent=2))
        self.finish()
#获取所有记录
    def get_all(self):
        ret = {'code':200,'content':''}
        try:
            item = self.db.query(WeKeyWord).all()
            ret['content'] = []
            for i in item:
                ret['content'].append({
                    'wid':i.wid,
                    'key':i.keyword,
                    'response':i.response
                    })
        except:
            ret['code'] = 500
            ret['content'] = "error"
        return ret
#添加一条记录
    def add_one(self):
        ret = {'code':200,'content':''}
        keyword = self.get_argument("key",default=None)
        response = self.get_argument("response",default=None)
        if not keyword or not response:
            ret['code'] = 400
            ret['content'] = u'参数缺少'
        else:
            item = WeKeyWord(keyword = keyword,response = response)
            try:
                self.db.add(item)
                self.db.commit()
                ret['code'] = 200
                ret['content'] = u'添加成功'
            except:
                ret['code'] = 500
                ret['content'] = "error"
        return ret 
#删除一条记录
    def delete_one(self):
        ret = {'code':200,'content':''}
        wid = self.get_argument("id",default=None)
        if not wid:
            ret['code'] = 400
            ret['content'] = u'参数缺少'
        else:
            try:
                item = self.db.query(WeKeyWord).filter(WeKeyWord.wid == int(wid)).one()
                self.db.delete(item)
                self.db.commit()
                ret['code'] = 200
                ret['content'] = u'删除成功'
            except Exception,e:
                ret['code'] = 500
                ret['content'] = str(e)
        return ret

        
    
    
      



