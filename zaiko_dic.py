zaiko_dic={}
zaiko_dic['cup']=10
zaiko_dic['dish']=20
zaiko_dic['base']=10

'''
def find_zaiko_dic(product,zaiko_dic):
    if product in zaiko_dic:
    	return zaiko_dic[product]
	

print (find_zaiko_dic("cup",zaiko_dic))
print (find_zaiko_dic("dish",zaiko_dic))
print (find_zaiko_dic("xxx",zaiko_dic))
'''
def inv_zaiko(zaiko_dic):
	inv_dic=dict()
	for k in zaiko_dic:
		w=zaiko_dic[k]
		if w not in inv_dic:
					# if inv_dic does not have w as a key
					# map  w-> [k]

				inv_dic[w]=[k]
		else:
			# append k as value of the list: inv_dic[w]
			inv_dic[w].append(k)
	return inv_dic

print (inv_zaiko(zaiko_dic))

#{10: ['base', 'cup'], 20: ['dish']}

