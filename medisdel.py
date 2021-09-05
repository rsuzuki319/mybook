#!/usr/bin/env python
# -*- coding: utf-8 -*-

file=open('h20191231del.txt')



memo=file.readline()
f=open('medisdel.txt',mode='a')
while memo:
	if (memo[0:13]):
		print (memo[0:13])
		f.write(memo[0:13])
		memo=file.readline()
    	
	
file.close()

f.close()