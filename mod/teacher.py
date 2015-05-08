# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from db import engine

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teacher'
    openid = Column(String(50),nullable = True)
    name = Column(String(50),primary_key = True)
    password = Column(String(50),nullable = False)
    state = Column(Integer,nullable = False)
    school = Column(String(50),nullable = True)
    room = Column(String(50),nullable = True)



def create_all():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    create_all()