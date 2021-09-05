#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Name:
	def __init__(self,start):
		self.data=start
	def __getslice__(self,low,high):
		return (self.data[low:high])


a=Name('abcde')

print (a.data[1:3])
