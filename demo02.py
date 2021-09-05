#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import random


file=open('happy.txt')
for kurikaeshi in range(1,12):
    memo=file.readline()
    new=''
    i=0
    for m in memo:
    	i=i+1
    	if m==' ':
    		new=new+'♡'
    	elif m=='*':
    		new=new+' '
    	elif m=='I':
    		new=new+'O'
    j=0
    while j<50-i:
    	new=new+'♡'
    	j=j+1

    time.sleep(1)
    print (new)
file.close()





