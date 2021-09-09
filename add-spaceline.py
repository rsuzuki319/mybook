#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv
#import random
args = sys.argv
j=0
m=0



af=args[2]
allf=open (af,'w')


with open(args[1],'r') as f:

    

    cnt1=cnt2=cnt3=0
    scount=0
    spaceflag=0
    k=0
    ccode='\n'
    cc=f.readline()
    while (cc):
        print (cc)    
        
        

        
        allf.write(cc)
        allf.write(ccode)
        
        k+=1
        cc=f.readline()
        
        if (k>50000):
            break
allf.close()




