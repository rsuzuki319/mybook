#!/usr/bin/env python
# -*- coding: utf-8 -*-

file=open('demo1.txt')
file2 =open('demo2.txt')


memo=file.readline()
memo2=file2.readline()
f=open('memo4.txt',mode='a')
while memo and memo2:
	if memo<memo2:
		print (memo)
		f.write(memo)
		memo=file.readline()
    	
	elif memo>memo2:
		print (memo2)
		f.write(memo2)
		memo2=file2.readline()
	elif memo==memo2:
		print (memo)
		f.write(memo)
		memo=file.readline()
		memo2=file2.readline()
    
    

else:	
	if len(memo)>0:
		while len(memo)>0:
			print (memo)
			f.write(memo)
			memo=file.readline()
	elif memo2:
		while memo2:
			print (memo2)
			f.write(memo2)
			memo2=file2.readline()
file.close()
file2.close()
f.close()


'''
file=open('demo_empty.txt')

for kurikaeshi in range(1,10):

    memo=file.readline()
    print (kurikaeshi)
    print (memo)
'''