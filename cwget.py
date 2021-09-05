#!/usr/bin/env python
# -*- encoding: utf-8 -*-
 
from __future__ import print_function, unicode_literals
import requests
import pprint
import json
 
#APIKEY = 'a457ce84d8c5de43c9e909ea49bb9e8f'
APIKEY= 'e21da3c399cf0fb644faaee7f64eea7b'
ENDPOINT = 'https://api.chatwork.com/v2'
#ROOMID = '152553520'
#ROOMID=' 152939278'
#MSGID='1183167621093130240'
#post_message_url = '{}/rooms/{}/messages'.format(ENDPOINT, ROOMID)
get_message_url = '{}/rooms'.format(ENDPOINT)
#get2_message_url = '{}/rooms/{}/messages'.format(ENDPOINT, ROOMID)
headers = { 'X-ChatWorkToken': APIKEY }
params = { 'body': 'I am fine and hope you are fine also' }



resp = requests.get(get_message_url,headers=headers)

pprint.pprint(resp.content)
#https://api.chatwork.com/v2/rooms/{room_id}/messages
rj=json.loads(resp.content)
print (rj)
for r in rj:
	print (r['room_id'])
	ROOMID=r['room_id']
	post_message_url = '{}/rooms/{}/messages'.format(ENDPOINT, ROOMID)
	resp = requests.post(post_message_url,
                    headers=headers,
                    params=params)
	rj=json.loads(resp.content)
	print (rj)

#print(resp.status_code)    
