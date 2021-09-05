#!/usr/bin/env python
# -*- encoding: utf-8 -*-
 
from __future__ import print_function, unicode_literals
import requests
import pprint
import json
import psycopg2
from datetime import timedelta
import time
import datetime
#
import argparse
def convhtml(htmlcont):
	import html2text
  
	#hc=htmlcont.decode('utf-8')
	h= html2text.HTML2Text()
	h.ignore_links = True
	h.escape_all=True
	text=h.handle(htmlcont)
	return text 
cont='[00000003    ]<p>薬はアストニールで6錠で11日分です。</p><p>&nbsp;</p>'
v=convhtml(cont)
print (v)
