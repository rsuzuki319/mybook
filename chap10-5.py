def average(a,b):
	return (a+b)/2

def sroot(num,low,high):
	for i in range(20):
		g=average(low,hight)
		if g**2==num:
			print (g)
		elif g**2>num:
			high=g
		else:
			low=g
	print (g)

	sroot(60,7,8)