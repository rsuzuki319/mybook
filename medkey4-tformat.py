#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv
import pprint

import mojimoji

from textformatting import ssplit
from pyknp import Juman
#this is used for medkey-sample.csv
def findkey(lk,word):
    print (word)
    for ll in lk:
        print (ll[0])

        if (ll[0]==word):
            print (ll[1])
            res=ll[1]
            break
    else:
        res=False
    return res

args = sys.argv
#print('args1:[{}]'.format(args[1]))
jumanpp = Juman(command='/home/ubuntu/local/bin/jumanpp')

with open(args[1]) as f:
    reader = csv.reader(f, delimiter='\t')
    ls = [row for row in reader]
with open(args[3]) as kk:
    reader = csv.reader(kk, delimiter='\t')
    lkey = [row for row in reader]
print (lkey)
kidc=dict()
for kk in lkey:
    kdic[kk[0]]=kk[1]

if (1):
    #print (ls)
    result_ls = []
    tags=[]
    seqs=[]
    k=0
    for l in ls:
        if (l):
            pass
        else:
            continue
        sq=l[1]
        k+=1
        wkeys=l[0].split('\n')
        print (wkeys)
        for cc in wkeys:
            keys=cc.split(')')
            tag=keys[0][1:2]
            print (tag)
        #tags.append(tag)
            if (len(keys)>1):
                cont=keys[1]
            else:
                print ("no conts")
                continue
        #cont=cont.replace(':',' ')

            cont=cont.replace('/',':')
#        print('step1:[{}]'.format(l[0]))

        #sentences = ssplit(cont)
            sentences=cont.split(':')
            print (sentences)

            result_strs = ''
            for sentence in sentences:
                if (sentence==''):
                    continue
                if sentence in kdic:
                    tag=kdic[sentence]

                result = jumanpp.analysis(sentence)


                result_str = ''
                first=1
                for mrph in result.mrph_list():

                    if result_str == '':

                        result_str = '{}'.format(mojimoji.han_to_zen(mrph.midasi))
                        #print('s1[{}]'.format(result_str))
                        if (first==1):
                            atag='B-'+tag
                            first=0
                        else:
                            atag='I-'+tag
                        result_ls.append([result_str,atag,sq])
                        #tags.append(atag)
                    
                        print (atag,sq)
                        result_str=''
                    else:
                        midasi_alt = mojimoji.han_to_zen(mrph.midasi)
                        if midasi_alt != "　":
                        
                            result_str = '{} {}'.format(result_str,midasi_alt)
                        #print('s4[{}]'.format(result_str))



    result_rows = []

    for i in range(len(result_ls)):
#        print('[{}][{}]'.format(result_ls[i],ls[i][1]))
        result_rows.append([ result_ls[i][0],result_ls[i][1],result_ls[i][2]])
    
    print(result_rows)
#    print(result_rows[0])

with open(args[2], 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(result_rows)
