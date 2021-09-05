#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv
#import pprint

#import mojimoji

#from textformatting import ssplit
#from pyknp import Juman

args = sys.argv
#print('args1:[{}]'.format(args[1]))
#jumanpp = Juman(command='/home/ubuntu/local/bin/jumanpp')
keylist=[]
with open(args[1]) as f:
    reader = csv.reader(f, delimiter=',')
    ls = [row for row in reader]


    result_ls = []
    result_rows=[]
    tags=[]
    k=0
    keydic=dict()
    for l in ls:
        if (l):
            pass
        else:
            continue


        k+=1
        #if (k>10000):
        #    break
        cont=l[2]
        #print (cont)
        #cont=cont.replace(':',' ')
        
        

        sentences = cont.split('\n')
        #sentences = cont.split('')
        for ss in sentences:
        
            #print (ss)
            if (ss==''):
                continue
        
            ww=ss.split(')')
            gg=ss.find(")")
            if (gg<0):
                continue
            #print (ww[0])
            #print (ww[1])
            wkey=ww[1]
            tag=ww[0][1:2]
            #print (wkey)
            #print ("tag ",tag)
            hkeys=wkey.split("/")

            #print (hkeys[0])
            
            if (len(hkeys)>1):
                xkey=hkeys[0]
            else:
                #print ("no /")
                #print (wkey)
                lkeys=wkey.split(":")
                ff=wkey.find(":")
                #print (ff)
                if (ff>0):
                    xkey=lkeys[0]
                    #print (xkey)
                    
                    
                else:
                    
                    xkey=wkey
                    #print (xkey)
                
            if (xkey in keydic):
                continue
            else:
                #print (xkey+'*'+tag)
                if (len(xkey)<50):
                    keydic[xkey]=tag

            #result_ls.append([ss,k])
    for kk in keydic:
        print (kk+':'+keydic[kk])
        keylist.append([kk,keydic[kk]])
        pass
        
with open(args[2], 'w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerows(keylist)        

    
'''
    for i in range(len(result_ls)):
#        print('[{}][{}]'.format(result_ls[i],ls[i][1]))
        result_rows.append([ result_ls[i][0],result_ls[i][1]])
    
    
    #print(result_rows[0])

with open(args[2], 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(result_rows)
'''
