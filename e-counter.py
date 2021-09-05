#!/usr/bin/env python
# -*- coding: utf-8 -*-

def e_counter(s):
	wd=dict()				
	for a in s:
		if a not in wd:
			wd[a]=1
		else:
			wd[a]+=1
	return wd				




def zeropad(no,l):
  i=0
  newno=no
  for i in range(l-len(no)):
      newno='0'+newno
      i=i+1
  return newno
 
print (zeropad('abc',8))
rr=e_counter('kakeyabuyaket')
print (rr)
