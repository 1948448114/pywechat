#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from db import engine

Base = declarative_base()

class WeKeyWord(Base):
    __tablename__ = 'keyword'
    wid = Column(Integer,primary_key=True)
    keyword = Column(String(64),nullable = False)
    response = Column(String(512),nullable = False)
    message_type = Column(String(16))


def create_all():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    create_all()