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
#APIKEY = 'a457ce84d8c5de43c9e909ea49bb9e8f'
#ROOMID = '152553520'
#ROOMID='152582262'
def convhtml(htmlcont):
	import html2text
  
	hc=htmlcont.decode('utf-8')
	
	h= html2text.HTML2Text()
	h.ignore_links = True
	h.escape_all=True
	text=h.handle(hc)
	print(text)
	return text  
def cwpost(arglist):
	text=arglist[0]
	rmid=arglist[1]
	print (text)
	print (rmid)
	textv=text
	APIKEY= 'e21da3c399cf0fb644faaee7f64eea7b'
	ENDPOINT = 'https://api.chatwork.com/v2'
	ROOMID=rmid
	#ROOMID='152939278'
	post_message_url = '{}/rooms/{}/messages'.format(ENDPOINT, ROOMID)
	print (post_message_url)
	headers = { 'X-ChatWorkToken': APIKEY }
	params = { 'body': textv }

	resp = requests.post(post_message_url,
                    headers=headers,
                    params=params)




	pprint.pprint(resp.content)
  
if __name__=='__main__':

	parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
	'''
	parser.add_argument(
      'text',
      help='text')
    '''
	parser.add_argument("-v", "--val",
        help="multiple values for this option",
        nargs="*",
        dest="vals"
    )
    
	args = parser.parse_args()
    
	cwpost(args.vals)

