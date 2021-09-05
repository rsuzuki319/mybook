#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
数字、英字のユニコード範囲：
---
数字半角[0-9] 0x30～0x39
数字全角[０-９] 0xFF10～0xFF19

英字半角・大文字[A-Z] 0x41～0x5A
英字全角・大文字[Ａ-Ｚ] 0xFF21～0xFF3A
英字半角・小文字[a-z] 0x61～0x7A
英字全角・小文字[ａ-ｚ] 0xFF41～0xFF5A
---
'''

import os
import re
import io
import unicodedata
 
text = u'ＡＢＣａｂｃ１２３カキク①（！％＠＃＄￥～　ABCabc123ｶｷｸ(!%@#$\~'
result=unicodedata.normalize("NFKC", text)
print (result)
print (chr(0x41))
y='Ａ'
#y=ord('Ａ')
print (y)
#print (int(0x41))
if (y>='Ａ' and y<='Ｚ'):
	print ("ZEn Capital:")
'''
for ch in range(26):
    print(chr(0xFF21 + ch))
'''
'''
upper = dict((0xFF21 + ch, 0x0041 + ch) for ch in range(26))
lower = dict((0xFF41 + ch, 0x0061 + ch) for ch in range(26))
number= dict((0xFF10 + ch, 0x0030 + ch) for ch in range(10))
 
#t = {**upper, **lower,**number}

text = u'ＡＢＣａｂｃ１２３カキク①（！％＠＃＄￥～　ABCabc123ｶｷｸ(!%@#$\~'

print(text.translate(number))
'''