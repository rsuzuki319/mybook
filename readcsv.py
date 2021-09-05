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






#file=open('/disk3/news/ns22-f')
#f=open('/disk3/news/news-22-0.csv',mode='w')
file=open('/disk3/news/ns44-a-v2')
f=open('/disk3/news/news-44.csv',mode='w')


memo=file.readline()
i=0
while (memo):
	memo=memo.strip()
	mm=memo.split(';')
	#print mm[1]
	if (mm[1]==''):
		i+=1
		memo=file.readline()
		continue
	print mm[3]
	flag=mm[3]
	kk=mm[1]
	kk=kk.replace('▽','*')
	#
	#　◇
	kk=kk.replace('◇','')
	kk=kk.replace('。','')
	#kk=kk.replace('【','')
	#【
	#kk=kk.replace('【','*')
	kk=kk.replace(',','')
	#print kk
	
	aa=kk.find('datePublished')

	
	if (aa):
		#aa=aa-1
		mk=kk[0:aa]
	else:
		mk=kk[0:]
		#print mk
	dd=mk.find('Yahoo!')
	if (dd):
		ymk=mk[0:dd]
	else:
		ymk=mk[:]
	#umk=mk.decode('utf-8')
	#zmk=jaconv.h2z(umk)
	#ymk=mk.encode('utf-8')
	
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