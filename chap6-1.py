#!/usr/bin/env python
# -*- coding: utf-8 -*-

#kan1=u'ーンアイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモマミムメモヤイユエヨラリルレロワイウエオ'
#kan2=u'ダヅデドガギグゲゴザジズゼゾバビブべボパピプペポ'
#kan3=kan1+kan2
katakana= u"ーァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヽヾ"

hiragana = u"ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖゝゞ" 
'''
kana=[]
hira=[]

for k in katakana:
	kana.append(k)
for k in hiragana:
	hira.append(k)
'''
file=open('2.txt')
word=''
mm=file.read()
memo=mm.decode('utf-8')
for m in memo:
    if m in katakana:
    	word=word+m
    else:
        print (word)
        word=''
file.close()


file=open('2.txt')
word=''
mm=file.read()
memo=mm.decode('utf-8')
for m in memo:
    if m in hiragana:
    	word=word+m
    else:
        print (word)
        word=''
file.close()


file=open('2.txt')
word=''
mm=file.read()
memo=mm.decode('utf-8')
for m in memo:
    if not (m in hiragana or m in katakana):
    	word=word+m
    else:
        print (word)
        word=''
file.close()