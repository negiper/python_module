#!/usr/bin/env python
#coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Table, MetaData, ForeignKey, Text
from sqlalchemy.orm import sessionmaker, mapper, relationship

engine = create_engine('mysql+pymysql://root:mysql@myserver2/blog')


#print engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False, index=True)
    password = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False, index=True)
    articles = relationship('Article', backref='author')
    userinfo = relationship('UserInfo', backref='user', uselist=False)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.username)

class UserInfo(Base):
    __tablename__ = 'userinfos'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    qq = Column(String(11))
    phone = Column(String(11))
    user_id = Column(Integer, ForeignKey('users.id'))


class Article(Base):
    __tablename__ = 'articles'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, index=True)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.title)

class article_tag(Base):
    __tablename__ = 'article_tag'

    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey('articles.id'))
    tag_id = Column(Integer, ForeignKey('tags.id'))


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, index=True)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.name)


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

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    
    Session_class = sessionmaker(bind=engine)

    Session = Session_class()

    obj1 = User(id=12, username='Joe', password='123', email='joe@qq.com')
    print obj1
    print obj1.username, obj1.id

    Session.add(obj1)

    Session.commit()
