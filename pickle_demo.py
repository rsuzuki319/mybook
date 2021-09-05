#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
import os
list_data=['a','b','c']
ll=pickle.dumps(list_data)
print (ll)
list_again=pickle.loads(ll)
print (list_again)
'''
cmd='ls -l'
fp=os.popen(cmd)
res=fp.read()
stat=fp.close()
print (stat)
print (res)
'''

filename='/s/medex/farm/vk2/osaka/u/manage/drive_yomi.py'
cmd='md5sum '+ filename
fp=os.popen(cmd)
res=fp.read()
stat=fp.close()
print (res)
filename='/s/medex/farm/vk2/tokyoc/u/manage/drive_yomi.py'
cmd='md5sum '+ filename
fp=os.popen(cmd)
res=fp.read()
stat=fp.close()
print (res)
