#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
import os
import re
import io
'''
def find(data,d):
    i=0
    while i<len(data):
        if data[i]==d:
            return i
        i=i+1
    return -1


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
            #error found
            result=result+data[0:]
            data=file.readline()
print (result)            




   