#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv
import argparse
import json

args=sys.argv
data=[]
res=[]
resall=[]
with open('predictions.txt','r') as gfile:
    seqno=0
    for line in gfile:
        res=[]
        wl=line.split(' ')
        for j in range(len(wl)):
            res.append(wl[j].strip('\n'))
        resall.append([seqno,res])
        seqno+=1

with open(args[1], 'w') as p:
    writer = csv.writer(p, delimiter=',')
    writer.writerows(resall)

        
'''
with open('test.json','r') as jfile:
    for line in jfile:
        data.append(json.loads(line))
for i in range(len(data)):
    
    for t in data[i]['tokens']:
        #print (t)
        pass
'''