#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import io

import requests
import json
url = 'https://api.chatwork.com/v2/me'
payload = {'body': 'dataaaaaaaaaaaaaaaaaaaaaaaaaa'}
headers = {'X-ChatWorkToken':'a457ce84d8c5de43c9e909ea49bb9e8f'}

#resp = requests.head(url)
#print (resp.status_code, resp.text, resp.headers)

r = requests.post(url, data=json.dumps(payload), headers=headers)
#response = requests.get("https://api.chatwork.com/v2/me", headers={"X-ChatWorkToken" : 'a457ce84d8c5de43c9e909ea49bb9e8f'})
print(r.status_code)    # HTTPのステータスコード取得
print(r.text)    # レスポンスのHTMLを文字列で取得