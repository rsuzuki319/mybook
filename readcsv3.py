#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jaconv
#https://pypi.org/project/jaconv/

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


ZEN = "".join(chr(0xff01 + i) for i in range(94))
HAN = "".join(chr(0x21 + i) for i in range(94))





file=open('/home/medex//nlpnews/ns22-vix.csv')
f=open('ns-22-vix-clean.csv',mode='w')


memo=file.readline()
i=0
while (memo):
	i+=1
	if (i>100):
		break
	print (memo.strip())
	mm=memo.split('\t')
	
	flag=mm[1]
	kk=mm[0]
	kk=kk.replace('▽','')
	#　◇
	kk=kk.replace('◇','')
	kk=kk.replace('【','')
	#【
	kk=kk.replace('【','')
	kk=kk.replace(',','')
	ukk=kk.encode('utf-8')
	#print kk
	for s in ukk:
		if (s in HAN):
			print (s)
		elif (s in ZEN):
			print (s)
		else:
			print ("bad"+s)

'''
	aa=kk.find('datePublished:')
	if (aa):
		mk=kk[0:aa]
		#print mk
		umk=mk.decode('utf-8')

		zmk=jaconv.h2z(umk)
		ymk=zmk.encode('utf-8')
		print (ymk)
		#zmk=han2zen(mk)
		f.write(ymk+'\t'+flag+'\n')
	memo=file.readline()
	i+=1
	print (i)
	if (i>10000):
		break
'''

file.close()
f.close()