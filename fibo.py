def fibo_s(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return fibo_s(n-1) + fibo_s(n-2)

print fibo_s(10)



def fibo(n):
	if n in done:
		return done[n]
	kekka=fibo(n-1) + fibo(n-2)
	done[n]=kekka
	return kekka

done={0:0,1:1}
print (fibo(10))

