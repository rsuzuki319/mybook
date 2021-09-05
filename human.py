#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Human:
	def setname(self,name):
		self.name=name
	def display(self):
		print self.name

'''
a=Human()
b=Human()


a.setname("山田太郎")
b.setname("大阪次郎")
a.display()
b.display()
'''
class Student(Human):
	def school(self,schoolname):
		self.schoolname=schoolname
	def displayschool(self):
		print (self.schoolname)
'''
s=Student()
s.name=('matsuo')
s.schoolname=('UCLA')
s.displayschool()
s.display()
'''

class Child(Student):
	def __init__(self,name):
		self.name=name
	def __add__(self,other):
		 return Child(self.name+other)
	def __mul__(self,other):
		self.name=self.name * other


c=Child('abcdefg')
c.display()

d=c+'wwwww'
d.display()

c*3
c.display()