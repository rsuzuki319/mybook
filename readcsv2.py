#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jaconv
#https://pypi.org/project/jaconv/
'''
def han2zen(han):
	ZEN = "".join(chr(0xff01 + i) for i in range(94))
	HAN = "".join(chr(0x21 + i) for i in range(94))

	ZEN2HAN = str.maketrans(ZEN, HAN)
	HAN2ZEN = str.maketrans(HAN, ZEN)
	return han.translate(HAN2ZEN)
# 全角から半角
	#print(ZEN.translate(ZEN2HAN))
# 結果
# !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~

# 半角から全角
	#print(HAN.translate(HAN2ZEN))

'''






file=open('/disk3/news/news-22-add')
f=open('news-22-1.csv',mode='w')


memo=file.readline()
i=0
while (memo):
	#need
	memo=memo.strip()
	mm=memo.split(';')
	#print mm[1]
	if (mm[1]==''):
		i+=1
		memo=file.readline()
		continue
	#print mm[2]
	flag=mm[2]
	kk=mm[1]
	kk=kk.replace('▽','*')
	#　◇
	kk=kk.replace('◇','')
	#kk=kk.replace('【','')
	#【
	#kk=kk.replace('【','*')
	kk=kk.replace(',','')
	#print kk
	aa=kk.find('style=')
	if (aa):
		mk=kk[aa+6:]
		a1=mk.find('>')
		if (a1):
			a1=a1+1
			mk=mk[a1:]
		bb=mk.find('</font></a>')
		if (bb):
			mk=mk[0:bb]
		#print mk
		umk=mk.decode('utf-8')
		zmk=jaconv.h2z(umk)
		ymk=zmk.encode('utf-8')
		
		#zmk=han2zen(mk)
		#need
		ymk=ymk.strip()
		print (ymk+';'+flag+'\n')
		f.write(ymk+';'+flag+'\n')
	memo=file.readline()
	i+=1
	print (i)
	if (i>10000):
		break
file.close()
f.close()