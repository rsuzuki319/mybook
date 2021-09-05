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
cont=''
data=file.readline()
while (data):
    cont=cont+data    
    data=file.readline()

s=find(cont,'@')    
e=find(cont,'$')

print (cont[s+1:e])          




   