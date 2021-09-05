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






file=open('/disk3/news/news-22a.csv')
f=open('/disk3/news/news-22add.csv',mode='w')
#file=open('/disk3/news/news-22.csv')
#f=open('/disk3/news/news-22a.csv',mode='w')


memo=file.readline()
i=0
while (memo):
	memo=memo.strip()
	memo=memo.strip('\n')
	mm=memo.split(';')
	#print (mm)
	#print mm[0]
	if (mm[0]==''):
		i+=1
		memo=file.readline()
		continue
	#print mm[1]
	flag=mm[1]
	kk=mm[0]
	kk=kk.replace('▽','*')
	#　◇
	kk=kk.replace('◇','')
	kk=kk.replace('\n','')
	#【
	#kk=kk.replace('【','*')
	kk=kk.replace(',','')
	#kk=kk.strip()
	#print kk
	aa=kk.find('datePublished:')
	if (aa):
		mk=kk[0:aa]
	else:
		mk=kk
		#print mk
	umk=mk.decode('utf-8')
	
	zmk=jaconv.h2z(umk)
	ymk=zmk.encode('utf-8')
	#print (ymk)
		#zmk=han2zen(mk)
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