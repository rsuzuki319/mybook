#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
import os
import re
import io
'''
import random
import substr

def find(data,d):
    i=0
    while i<len(data):
        if data[i]==d:
            return i
        i=i+1
    return -1
'''
for k in range(20):
    r=random.random()
    print (r)
'''
for k in range(20):
    r=random.randint(1,6)
    print (r)


data='abcdefg'
print (substr.substr(data,1,4))
'''
file=open('data.txt')
result=''
data=file.readline()

while (data):
        
    
    s=find(data,'@')
    if s>0:
        
        e=find(data,'$')
        if e>0:
            result=result+data[s+1:e]
            break
        else:
            result=result+data[s+1:]
            
            data=file.readline()
            continue
    else:
        e=find(data,'$')
        if e>0:
            result=result+data[:e]
            break
        else:
            data=file.readline()
print (result)            

'''


   