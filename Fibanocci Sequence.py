def Fibonacci(n):
	if n == 0:
		return 0
	elif n == 1 or n == 2:
		return 1

	else:
		return Fibonacci(n-1) + Fibonacci(n-2)


n = int(input("Enter a num: "))
print("Fibanocci position at",n,"is: ",Fibonacci(n-1))
