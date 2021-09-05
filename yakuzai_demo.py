#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
number=['0','1','2','3','4','5','6','7','8','9']
inputr=open("yakusample.txt")

print ("read all content to a string")
s=inputr.read()

#print (s)
rr=s.split()
print (rr)
nn=0
rp=1
yohoari=0
yakuzai=[]
yoryo=[]
yoho=[]
hi=[]
yy=dict()
hh=dict()
for r in rr:
	if (r[0]=='-'):
		continue
	if (r==str(rp)):
		print ("RP",rp)
		nn=1
		rp=rp+1
		continue
	else:
		#print ("yakuza-name",r.decode('utf-8'))


		if (nn==1):
			print (r.decode('utf-8'))
			yakuzai.append(r)
			nn=nn+1
			continue
		if(nn==2):
			ss=''
			for s in r:
				if s in number:
					ss=ss+s
			print ss
			yoryo.append(ss)
			
			nn=nn+1
			continue
		if (nn==3 and r.decode('utf-8')!='..'):
			print (r.decode('utf-8'))
			yakuzai.append(r)
			nn=2
			continue
		if (nn==3 and r.decode('utf-8')=='..'):
			print (r.decode('utf-8'))
			yohoari=1
			nn=0
			continue

		if (yohoari==1):
			print (r.decode('utf-8'))
			yoho.append(r)
			yy[rp-1]=r
			nn=0
			yohoari=2
			continue
		if (yohoari==2):
			print (r)
			ss=''
			for s in r:
				if(s=='('):
					continue
				if (s==')'):
					break
				if s in number:
					ss=ss+s
			print ss
			
			hi.append(ss)
			hh[rp-1]=ss
			nn=0
			yohoari=0
			continue

print (yakuzai)
print (yoryo)	
print (yoho)
print (hi)
print (yy[1])
print (hh[1])

print (yy[2])
print (hh[2])














inputr.close()	