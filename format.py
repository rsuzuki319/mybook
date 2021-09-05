#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
mgrade=90

my="数学の点数は" + '%d' % mgrade
print (my)

egrade=80
my="数学の点数は %d で英語の成績は%d です" % (mgrade,egrade)
print (my)


print (os.path.exists('my_grade.txt'))