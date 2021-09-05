#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
import os
import re
import io
'''
import string
data='''AAAAAAAAAAAAAAAAAA BBBBBB
薬剤:
1 アーチスト錠１０ｍｇ 　1錠
  .. 頓用 (1)日分
--------------------------------------@ 

EEEE
FFF

'''
def f_substr(data):

        
    ll=[]
    result=''
    left=''
    i=string.find(data,'薬剤:')
    if i>0:
        
        e=string.find(data,'@')
        if e>0:
            result=data[i:e+1]
            left=data[0:i-1]+data[e+1:]
        else:
            result=data[i:]
            left=data[0:i-1]
            
    #print (result)            
    #print (left)

        ll=[result,left]
    #print (ll[0])
    else:
        ll=['','']
    return ll

if __name__ == '__main__':
    
    ll=f_substr(data)
    print (ll[0])
    print (ll[1])
    


   