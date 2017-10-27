#coding=utf-8
import inspect
import os.path

class Person(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def hello(self):
		'''获取函数调用栈信息'''
		#print inspect.stack()
		print u'本函数由', os.path.abspath(inspect.stack()[-1][1]),u'中的', inspect.stack()[-1][4][0].strip(),\
			  u'第(%d)行调用' % (inspect.stack()[-1][2],)
		print u'该函数来自：',
		print os.path.abspath(inspect.stack()[0][1]),':', '.'.join([self.__class__.__name__,inspect.stack()[0][3]])
		print 'Hello! My name is %s' % self.name
	
	def info(self, native_place='', addr='', phone=''):
		'''获取函数所需参数'''
		print 'Info of %s:' % (self.name,)
		print '%s\t%s\t%s\t%d' % (native_place, addr, phone,self.age)
if __name__ == "__main__":
	p1 = Person('Tom', 12)
	p1.hello()
	print
	print u'函数info所需参数:'
	print inspect.getargspec(p1.info).args
	p1.info('Dali', 'Kunming', '123456')
	