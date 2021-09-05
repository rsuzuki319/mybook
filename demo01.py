#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import random
import pygame
'''
file=open('happy.txt')
for kurikaeshi in range(1,20):
    memo=file.readline()
    time.sleep(1)
    print (memo)
file.close()





front=''
back=''
middle=''

for i in range(20):
	print (front+'*'+middle+'*'+back)
	time.sleep(1)
	front=front+' '
	middle=middle+' '
for i in range(21):
	f=front[0:20-i]
	m=middle[0:20-i]
	print (f+'*'+m+'*'+back)
	time.sleep(1)
'''


while (1):
	su='S';
	for i in range(5):
		su=su+'u'
		print (su)
		time.sleep(1)
		ha='H'
	for i in range(8):
		ha=ha+'a'
		print (ha)
		time.sleep(1)

'''

while (1):
	su='S';
	p=random.randint(1,6)
	for i in range(p):
		su=su+'u'
		print (su)
		time.sleep(1)
		ha='H'
	m=random.randint(1,6)
	for i in range(m):
		ha=ha+'a'
		print (ha)
		time.sleep(1)
'''