#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import codecs
def acounter(ss):
	a=['a','b','c','d']
	v=[0,0,0,0]
	for k in range(len(ss)):
		for i in range(4):
			if (ss[k]==a[i]):
				v[i]=v[i]+1
				break
			i+=1
		else:
			print ("NO character ",ss[k])
		k+=1
	return v
    

rr=acounter('aabccde')
print (rr)
