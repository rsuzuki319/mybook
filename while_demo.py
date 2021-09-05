#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import io

val_valid=False
while val_valid==False:

	try:
		val=''
		val=input()
		intval=int(val)
		val_valid=True
	except ValueError:
		print ('retype correct number')

	except KeyboardInterrupt:
		print ('Do not stop program ')

	print ('Right',val)



	
