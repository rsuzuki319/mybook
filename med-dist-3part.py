#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv
import random
args = sys.argv
j=0
m=0
'''
with open(args[1],'r') as f:

    cc=f.readline()
    while (cc):
        print ("code:",cc.decode("utf-8"))
        cc=f.readline()
'''    

dr=args[2]
trf=dr+"/train.tsv"
tef=dr+"/test.tsv"
df=dr+"/dev.tsv"


trainf=open (trf,'w')
testf=open (tef,'w')
devf=open (df,'w')


limit=float(args[3])
limit1=limit*0.8
limit2=limit*0.1
limit3=limit*0.1

with open(args[1],'r') as f:
    cc=f.readline()
    print (cc)

    cnt1=cnt2=cnt3=0
    scount=0
    spaceflag=0
    k=0
    while (cc):
        
        m=random.randint(1,limit)
        #print (m)

        l=cc.split('\t')
        
        if (l[0]=='\n'):
            print (l)
            print ("space line")
            scount+=1 
            spaceflag=1  
        else:
            spaceflag=0     
       
        
        if (cnt1<limit1):
            #cnt1+=1
            trainf.write(cc)
            if (spaceflag==1):
                cnt1+=1

        elif (cnt2<limit2):
            testf.write(cc)
            
            if (spaceflag==1):
                cnt2+=1            
        elif (cnt3<limit3):
            devf.write(cc)
            if (spaceflag==1):
                cnt3+=1
            
        else:
            print ("no more distribute")
        k+=1
        cc=f.readline()
        print (k,cnt1,cnt2,cnt3,scount)
        if (k>50000):
            break

trainf.close()
testf.close()
devf.close() 


    


