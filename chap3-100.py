#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time,os

def  is_product(product_id,product_list):
    if (product_id  in product_list):
    	return True   	
    else:
    	return False


pr=["1","2","3"]

b=is_product("5",pr)
 
print (b)