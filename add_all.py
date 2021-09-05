def add_all(*args):
	total=0
	for i in args:
		total +=i
	return total


print (add_all(1,2,3,4,5,6,7,8,9,10))


w_dic={'a':'apple','b':'boy','c':'cat'}

wt=w_dic.items()

print (wt)


w_dic_again=dict(wt)
print (w_dic_again)


tel_cho={}
tel_cho['yamada','taro']='090-333-1111'
tel_cho['tanaka','jiro']='090-333-2222'
print (tel_cho)


for lname,fname in tel_cho:
	print (lname, fname, tel_cho[lname,fname])


