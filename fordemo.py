#!/usr/bin/env python
# -*- coding: utf-8 -*-

file=open('memo3.txt')

#read all data at once
#memo3=file.read()
#memo=memo3.decode('utf-8')

'''
memo='今日は山田さんと田中さんが私の家（松尾）にやってきてBQパーティーをしました'
for x in memo:
    #print (x)
    if x==u'松':
            print ('Exists')
            break

'''
#memo=u'今日は山田さんと田中さんが私の家（松尾）にやってきてBQパーティーをしました'
memo=u'今日は山田さんと田中さんと松永さんが私の家（松尾）にやってきてBQパーティーをしました'

kaisu=0
for x in memo:
    print (x)
    if x==u'松':
            kaisu=kaisu+1
            print (kaisu)
            continue




'''
file=open('demo_empty.txt')

for kurikaeshi in range(1,10):

    memo=file.readline()
    print (kurikaeshi)
    print (memo)
'''