def even(x):
	while(x!=0):
		if x%2==0:
			yield x
			#return x
		x-=1
for i in even(8):
	print("manoj")
	print(i)
