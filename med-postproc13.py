#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv
import pprint
import re

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

            tagdic[ll[0]]=ll[1]
            
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

def createtag(top,tag,wd):
    wline=tag[0]+')'
    wlist=''
    for ww in wd:
        wlist=wlist+ww+':'
    res=wline+wlist
    return res
#main    
args = sys.argv
tagdic=dict()
tagdic2=dict()

wd=[]
tag=[]
top=[]
second=[]
lines=[]
#print('args1:[{}]'.format(args[1]))

#
#med-dlk0811c2,tsv
with open(args[1]) as f:
    reader = csv.reader(f, delimiter='\t')
    lk = [row for row in reader]

dlfile=open(args[2],'w')
record=[]
if (1):
    k=0
    pretag=''
    paracount=0
    count=0
    first=1
    tag=''
    cont=0
    o_ari=0
    for l in lk:
        k+=1
        if (k>150000):
            break
        print (l)  
        if (len(l)==0):
            record.append(['\n'])
            dlfile.write('\n')
            print ("sentence break")
            o_ari=0
            cont=0
            pretag=''
            tag=''
            continue
        
        
        if (l[1][0:1]=='O'):
            #the tag is O
            #print (l[1])
            record.append([l[0],l[1]])
            dlfile.write(l[0]+'\t'+l[1]+'\n')
            o_ari=1
            continue
            #tag =='I' continuous
        elif (l[0]=='なし' or l[0]=='あり'):
            print ("nashi.ari")
            maintag=l[1][2:3]
            if (tag):
                newtag='I-'+tag
            else:    
                newtag='I-'+maintag
            record.append([l[0],newtag])
            dlfile.write(l[0]+'\t'+newtag+'\n')
            o_ari=0
            continue
        elif (l[0]=='．'):
            print ("ten ari")
            maintag=l[1][2:3]
            if (tag):
                newtag='I-'+tag
            else:    
                newtag='I-'+maintag
            record.append([l[0],newtag])
            
            dlfile.write(l[0]+'\t'+newtag+'\n')
            o_ari=0
            continue
        elif (l[1][0:1]=='I'):
            print (l[1])
            print ('continue ?',cont)
            maintag=l[1][2:3]

            if (maintag == tag or maintag=='*'):
                if (maintag=='*'):
                    tag='P'
                    maintag='P'
                if (o_ari==1):
                    print ("O-ari")
                    newtag='B-'+tag
                    record.append([l[0],newtag])
                    dlfile.write(l[0]+'\t'+newtag+'\n')
                    #tag=maintag
                    o_ari=0
                    #break cont?
                    cont=1
                         
                else:
                    print ("O-nashi")
                    newtag='I-'+tag
                    record.append([l[0],newtag])
                    dlfile.write(l[0]+'\t'+newtag+'\n')
                    o_ari=0
            else:
                print ("diff tag start")
                cont=0
                if (l[0].strip=='なし' or l[0].strip=='あり'):
                    print ("nashi.ari")
                    print (tag)
                    newtag='I-'+tag
                    record.append([l[0],newtag])
                    dlfile.write(l[0]+'\t'+newtag+'\n')
                    cont=1
                    
                else:   
                    tag=maintag
                
                    newtag='B-'+tag
                    record.append([l[0],newtag])
                    dlfile.write(l[0]+'\t'+newtag+'\n')
                    print ("new tag")
                    print (newtag)
                    o_ari=0
                    
        
        elif (l[1][0:1]=='B'):
            print (l[0])
            cont=1
            maintag=l[1][2:3]
            if (maintag == tag or maintag=='*'):
                if (maintag=='*'):
                    maintag='P'
                    tag='P'
                if (o_ari==1):
                    newtag='B-'+tag
                    record.append([l[0],newtag])
                    dlfile.write(l[0]+'\t'+newtag+'\n')
                    #tag=maintag
                    o_ari=0

                else:
                    newtag='I-'+tag
                    record.append([l[0],newtag])
                    dlfile.write(l[0]+'\t'+newtag+'\n')
                    o_ari=0                
                
                
            else:
                print ("diff tag start")
                
                    
                if (maintag=='*'):
                    maintag='P'
                    tag='P'
                else: 
                    tag=maintag
                
                newtag='B-'+tag
                record.append([l[0],newtag]) 
                dlfile.write(l[0]+'\t'+newtag+'\n')           

dlfile.close()           
            
          


           
  
        
        



with open(args[3], 'w') as w:
    writer = csv.writer(w, delimiter='\t')
    writer.writerows(record)
       

        
        


