#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import codecs
def hash(wstring, tablesize):
    sum = 0
    for pos in range(len(wstring)):
        sum = sum + ord(wstring[pos])

    return sum%tablesize

word=[]
for i in range(100):
	word.append([])
word[hash('apple',100)]=['リンゴ']
word[hash('banana',100)]=['バナナ']
word[hash('mango',100)]=['マンゴ']

print (word[hash('apple',100)][0])
print (word[hash('banana',100)][0])
print (word[hash('mango',100)][0])