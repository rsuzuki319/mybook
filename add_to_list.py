#!/usr/bin/env python
# -*- coding: utf-8 -*-

def add_to_list(wl,ww):
	#wl=wl.append(ww)
	#do not assign to wl: wrong 
	wl.append(ww)

	return wl


def add_to_list2(wl,ww):
	new=wl+ww
	return new

wl=[1,2,3]
wl2=[5,6,7]
ww=4
ww2=[8]

print (add_to_list(wl,ww))

print (add_to_list2(wl2,ww2))
