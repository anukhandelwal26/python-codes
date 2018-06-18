def factorial(num):
	if num==1:
		return num
	else:
		return num*factorial(num-1)

num=int(raw_input("enter a number"))

if num<0:
	print("factorial cannot be of negative number")
elif num==0:
	print("factorial is 1")
else:
	print("factorial is",factorial(num))
