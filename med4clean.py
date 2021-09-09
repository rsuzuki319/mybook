#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv
args = sys.argv
#print('args1:[{}]'.format(args[1]))
#jumanpp = Juman(command='/home/ubuntu/local/bin/jumanpp')

with open(args[1]) as f:
    reader = csv.reader(f, delimiter=',')
    ls = [row for row in reader]


    result_ls = []
    result_rows=[]
    tags=[]
    k=0
    for l in ls:
        if (l):
            pass
        else:
            continue



        cont=l[1]
        cdate=l[0]
        #cont=cont.replace(':',' ')
        
        

        sentences = cont.split('。')
        for ss in sentences:
            
            if (ss==''):
                continue
        

            result_ls.append([ss,k])
    
    	k+=1   

    

    for i in range(len(result_ls)):

        result_rows.append([ result_ls[i][0],result_ls[i][1]])
        result_rows.append([ '',result_ls[i][1]])
    
    
    

with open(args[2], 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(result_rows)
