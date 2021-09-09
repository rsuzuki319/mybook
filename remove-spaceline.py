#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv
#import random
args = sys.argv
j=0
m=0



af='allkarte.tsv'
allf=open (af,'w')


with open(args[1],'r') as f:
    cc=f.readline()
    print (cc)

    cnt1=cnt2=cnt3=0
    scount=0
    spaceflag=0
    k=0
    while (cc):
        
        
        

        l=cc.split('\t')
        
        if (l[0]==' '):
            print (l)
            print ("space line")
            cc=f.readline()
            if (cc[0:1]==' '):
                ccode='\n' 
                allf.write(ccode)
        else:
            allf.write(cc)
        
        k+=1
        cc=f.readline()
        
        if (k>50000):
            break
allf.close()

with open(args[1]) as h:
    reader = csv.reader(h, delimiter='\t')
    lg = [row for row in reader]
for i in range(len(lg)):
    if (lg[i][0]==' '):
        j+=1
    else:
        m+=1
print (j,m)     


