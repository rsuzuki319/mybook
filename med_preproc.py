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
tagdic2['血圧']=1
tagdic['脈拍']=1
tagdic['身長']=1
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
with open(args[2]) as g:
    reader = csv.reader(g, delimiter=',')
    lg = [row for row in reader]
keydic=dict()
print (len(lg))
for ee in lg:
    if ee[0] in keydic:
        continue
    else:

        keydic[ee[0]]=ee[1]
        #print (ee[0])


if (1):
    k=0
    pretag=''
    paracount=0
    count=0
    for l in lk:
        k+=1
        if (k>200000):
            break
        if (l):
            pass
        else:
            continue
        #print (l[1])

        maintag=l[1][2:3]
        
        if (l[1][0:1]=='O'):
            #print (newline)

            continue
        if (l[1][0:3]=='B-O'):
            word=l[0].strip()

            #print (word)
            if (word in tagdic):
                print ("exist in tagdic")
                paracount=1
                count=0
                top.append(word)
                
                wd.append(word)
                tag=['O']
            elif (word in tagdic2):
                print ("exist in 2tagdic")
                paracount=2
                top.append(word)
                
                wd.append(word)
                tag=['O']

            else:
                #print ("NO in dic")
                if (paracount==1):

                    wd.append(word)
                    tag=['O']
                    res=createtag(top,tag,wd)
                    print (res)
                    lines.append([res])
                    top=[]
                    wd=[]
                elif (paracount==2):
                    if (count==0):
                        count+=1
                        top.append(word)                
                        wd.append(word)
                        tag=['O']
                        #print ('frist no')
                    elif (count==1):
                        #print ('second no')
                        wd.append(word)
                        tag=['O']
                        res=createtag(top,tag,wd)
                        print (res)
                        lines.append([res])
                        top=[]
                        wd=[]                        


            pretag="B-O"
  
        elif (l[1][0:3]=='B-T'):

            word=l[0].strip()
            if (pretag=='I-T'):
                pass

            else:    
                if (len(top)>0):
                    res=createtag(top,tag,wd)
                    print (res)
                    lines.append([res])
                    top=[]
                    wd=[]
            top.append(word)
            wd.append(l[0].strip())
            tag=["T"] 
            pretag='B-T'  
        #************************************ 
        elif (l[1][0:3]=='B-P'):

            word=l[0].strip()
            if (pretag=='I-P'):
                pass

            else:    
                if (len(top)>0):
                    res=createtag(top,tag,wd)
                    print (res)
                    lines.append([res])
                    top=[]
                    wd=[]
            top.append(word)
            wd.append(l[0].strip())
            tag=["P"] 
            pretag='B-P' 
        #**************************************                   
        elif (l[1][0:3]=='I-T'):
            word=l[0].strip()
            if (maintag in tag):
                wd.append(l[0].strip())
            else:
                print ("new tag without B")

                res=createtag(top,tag,wd)
                print (res)
                lines.append([res])
                tag=[maintag]
                wd=[l[0].strip()]
                top=[] 
            pretag='I-T'           
            

        elif (l[1][0:1]=='B'):
            word=l[0].strip()
            if (len(top)>0):
                    res=createtag(top,tag,wd)
                    print (res)
                    lines.append([res])
                    top=[]
                    wd=[]
            top.append(word)
            wd.append(l[0].strip())
            tag=[maintag] 
            pretag='B-' + maintag       

        elif (l[1][0:1]=='I'):
            word=l[0].strip()
            if (maintag in tag):
                wd.append(l[0].strip())
            else:
                print ("new tag without B")

                res=createtag(top,tag,wd)
                print (res)
                lines.append([res])
                tag=[maintag]
                wd=[l[0].strip()]
                top=[]
            pretag='I-'+maintag
        else:
            print ("error no tag")




with open(args[3], 'w') as w:
    writer = csv.writer(w, delimiter=',')
    writer.writerows(lines)
       
