#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
import os
import re
import io
'''
def substr(data,s,l):
    
    if len(data)>0:
        if s<len(data):
            if l<len(data):
                result=data[s:l]
                
            else:
                result=data[s:]
                
        else:
            print ("s is too big")
            result=-1
    else:
        print ("string is null")
        result=-1
    return result


#main
if __name__ == '__main__':

    substr(*arg)




   