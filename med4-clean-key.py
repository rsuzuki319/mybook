#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv
#import pprint

#import mojimoji

#from textformatting import ssplit
#from pyknp import Juman
def clean(ss):
    
            #ww=ss.split(')')
            gg=ss.find(")")
            if (gg<0):
                res=ss
                

            
            
            else:

               
                ff=ss.find("/")
                if (ff<0):
                    hh=ss.find(":")
                    if (hh<0):
                        res=ss+'/'
                        
            
            
                    else:
                        res=ss[0:hh]+'/'+ss[hh:]
                    
                    
                else:
                    hh=ss.find(":")
                    if (hh<0):
                        res=ss+'/'
                        
            
            
                    else:
                        res=ss[0:hh]+'/'+ss[hh:]
                    

                    
                    res=ss
            
            return res       
                


args = sys.argv
#print('args1:[{}]'.format(args[1]))
#jumanpp = Juman(command='/home/ubuntu/local/bin/jumanpp')

with open(args[1]) as f:
    reader = csv.reader(f, delimiter=',')
    ls = [row for row in reader]

#    r = ls[4]
#    print(r)
#    sentences = ssplit(ls[4][0])
#    print('step1 : {}'.format(sentences))

#    for i in range(len(l)):        
#        print('step1-{} : {}'.format(i,l[i][0]))
#        sentences = ssplit(l[i][0])
    #print (ls)
    result_ls = []
    result_rows=[]
    tags=[]
    k=0
    for l in ls:
        if (l):
            pass
        else:
            continue



        cont=l[2]
        #cont=cont.replace(':',' ')
        
        

        sentences = cont.split('\n')
        for ss in sentences:
            #print (ss)
            if (ss==''):
                continue

        
            st=clean(ss)
            result_ls.append([st,k])
        k+=1

    

    for i in range(len(result_ls)):
#        print('[{}][{}]'.format(result_ls[i],ls[i][1]))
        result_rows.append([ result_ls[i][0],result_ls[i][1]])
    
    
    #print(result_rows[0])

with open(args[2], 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(result_rows)
