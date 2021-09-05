#!/usr/bin/env python
# -*- coding: utf-8 -*-

zaiko_list=[["1",100],["2",150]]

def find_zaiko(product_id,zaiko_list):
    
    for pp in zaiko_list:
    	
        if pp[0]==product_id:
			print ("find")
			return_value=pp[1]
			
			
	
			return return_value
    return 0

print (find_zaiko("10",zaiko_list))