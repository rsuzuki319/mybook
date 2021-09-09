# -*- coding: utf-8 -*-
import re
import io
import os, sys, time, getopt
import subprocess
import csv

lf=os.system("ls /tmp/test>/tmp/lslog.txt")
#print (lf)
with open('/tmp/lslog.txt') as f:
	reader = csv.reader(f, delimiter='\n')
	ls = [row for row in reader]
for k in range(len(ls)):
	fname=ls[k][0]
	print (fname)	

	status=os.system("scp -i /home/medex/lcm.pem"+"  /tmp/"+fname+" ubuntu@xxxxxxx:/tmp")
