#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv
import pprint
import re
#python med-preproc2.py med-dlk0811c2.tsv  med-cleankey0811.tsv medkey-pair.tsv med-out3-dlk0811.tsv med-res3-dlk0811.tsv
#import mojimoji

#from textformatting import ssplit
#from pyknp import Juman
def find_tag(lg,w):
    for ll in lg:
        #print (ll[0])
        if (ll[0]==w):
            wtag=ll[1]
            break
    else:
        wtag='O'
    return wtag
def createdic(lg,seqno):
    tagdic=dict()
    for ll in lg:
        
        if (ll[2]==seqno):
            tag=ll[1]
            if (tag[2:3]=='*'):
                newtag=tag[0:2]+'P'
                tagdic[ll[0]]=newtag
            else:
                tagdic[ll[0]]=tag
            
    print (tagdic)
    return tagdic
def find_keyp(lg,w):
    for ll in lg:
        #print (ll[0])
        if (ll[0]==w):
            wtag=True
            break
    else:
        wtag=False
    return wtag
#main    
args = sys.argv
tagdic=dict()
#print('args1:[{}]'.format(args[1]))

#python med-preproc.py med2-v2-sample.tsv medkey-res-sample.tsv med-out-sample.tsv
#med-dlk0811c2.tsv
#med-addline12.csv
with open(args[1]) as f:
    reader = csv.reader(f, delimiter='\t')
    lk = [row for row in reader]
#med-cleankey0811.tsv
with open(args[2]) as g:
    reader = csv.reader(g, delimiter='\t')
    lg = [row for row in reader]

        
#medkey2-pair.tsv
with open(args[3]) as kp:
    reader = csv.reader(kp, delimiter='\t')
    lkp = [row for row in reader]
    kdic=dict()
    for pp in lkp:
        kdic[pp[0]]=pp[1]


if (1):
    stfile=open(args[4], 'w')
    k=0
    res=[]
    first=1
    seq=0
    st=''
    cont=[]
    #initial dic
    tagdic=createdic(lg,seq)
    #print (tagdic)
    #sentence
    for l in lk:
        print (l)
    
        if (len(l)<2):
            print ("No tag or sentence")
            stfile.write('\n')
            continue

        if (seq==l[1]):

            print (l[0])
            words=l[0].split()
            
            
            for w in words:
                if w in kdic:
                    wtag=kdic[w]
                    res.append([w,wtag])
                else:
                       
                    if w in tagdic:
                        wtag=tagdic[w]
                        if (w=='なし' or w=='あり'):
                            wwtag='I-'+wtag[2:1]
                            res.append([w,wwtag])
                        else:
                            res.append([w,wtag])
                    else:                    
                        wtag='O'
                    
                    
                    
            
                cont.append([w,wtag])
                stfile.write(w+'\t'+wtag+'\n')
            
           
                
        else:
            
            cont.append(['\n']) 
            
            #new seqno is set now 
            seq=l[1]
            tagdic=createdic(lg,seq)

            
            words=l[0].split()
            
            k=0
            for w in words:
                if w in kdic:
                    wtag=kdic[w]
                    res.append([w,wtag])
                else:
                       
                    if w in tagdic:
                        wtag=tagdic[w]
        
                        res.append([w,wtag])
                    else:                    
                        wtag='O'
        
                st=w+'\t'+wtag+'\n'
                cont.append([w,wtag])
                stfile.write(st)
       
           
         

        
stfile.close()   

with open(args[5], 'w') as w:
    writer = csv.writer(w, delimiter='\t')
    writer.writerows(res)

    
with open(args[6], 'w') as wf:
    writer = csv.writer(wf, delimiter='\t')
    writer.writerows(cont)       

        
        


