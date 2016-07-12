# 20.py - this is a program for finding factorial using for loop. 
def factorial(n):
	fact = 1
	for i in range(1, n+1):
		fact = fact * i
	print(fact)
factorial(5)
