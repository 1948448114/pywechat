# -*- coding: utf-8 -*-
import tornado.web
from tornado.httpclient import HTTPRequest, HTTPClient
from config import LOCAL,candidates
import random

class ListHandler(tornado.web.RequestHandler):
    def get(self):
        number = []
        for count in range(0,len(candidates)):
            number.append(count)
        length = len(candidates)
        random.shuffle(number)
        self.render('list.html', candidate = candidates,number = number,LOCAL = LOCAL,length = length)