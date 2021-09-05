#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv

args = sys.argv

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
        
        cont=l[2]
        
        

        sentences = cont.split('\n')
        
        for ss in sentences:
        
            #print (ss)
            if (ss==''):
                continue
        
            ww=ss.split(')')
            gg=ss.find(")")
            if (gg<0):
                continue
            
            wkey=ww[1]
            tag=ww[0][1:2]
           
            hkeys=wkey.split("/")

            
            
            if (len(hkeys)>1):
                xkey=hkeys[0]
            else:
               
                lkeys=wkey.split(":")
                ff=wkey.find(":")
                
                if (ff>0):
                    xkey=lkeys[0]
                    
                    
                    
                else:
                    
                    xkey=wkey
                   
                
            if (xkey in keydic):
                continue
            else:
                
                if (len(xkey)<50):
                    keydic[xkey]=tag

            
    for kk in keydic:
        print (kk+':'+keydic[kk])
        keylist.append([kk,keydic[kk]])
        pass
        
with open(args[2], 'w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerows(keylist)        

    

