vendor_dic={}
vendor_dic['cup']=['Hasami','box-A']
vendor_dic['dish']=['Echizen','box-B']
vendor_dic['base']=['Arita','box-C']


def find_vendor_dic(product,vendor_dic):
    if product in vendor_dic:
    	return vendor_dic[product]

def list_cont(w_list):
	json_form='{'+'"vendor":'+'"'+w_list[0]+'"'+","+'"unit":'+'"'+w_list[1]+'"'+"}"
	print (json_form)


list_cont(find_vendor_dic("cup",vendor_dic))
list_cont(find_vendor_dic("dish",vendor_dic))
list_cont(find_vendor_dic("base",vendor_dic))



'''
def inv_vendor(vendor_dic):
	inv_dic=dict()
	for key in vendor_dic:
		w=vendor_dic[key]
		if w not in inv_dic:
				inv_dic[w]=[key]
		else: 
			inv_dic[w].append(key)
	return inv_dic
'''

#print (inv_vendor(vendor_dic))