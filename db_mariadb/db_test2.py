#!/usr/bin/env python
#coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Table, MetaData
from sqlalchemy.orm import sessionmaker, mapper

engine = create_engine('mysql+pymysql://root:mysql@myserver2/blog')


#print engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False, index=True)
    password = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False, index=True)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.username)

Base.metadata.create_all(engine)


'''
meta = MetaData()
stus = Table('stus', meta,
              Column('id', Integer, primary_key=True),
              Column('name', String(20)),
              Column('password', String(20)))

class Stu(object):
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password
mapper(Stu, stus)
'''

Session_class = sessionmaker(bind=engine)

Session = Session_class()

obj1 = User(id=10, username='Jenny', password='123', email='jenny@qq.com')
print obj1.username, obj1.id

Session.add(obj1)
print obj1.username, obj1.id

Session.commit()
