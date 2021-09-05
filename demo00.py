#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time,os

'''
print ('      *       *'     )
print ('   *    *  *     *'  )
print (' *        *        *')
print ('*                  *')
print ('*                  *')
print (' *                *' )
print ('  *             *'   )
print ('    *         *'     )
print ('      *     *'       )
print ('         *     '     )
'''
'''
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