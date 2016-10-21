#fibonacci: 0,1,1,2,3,5,8,13,21,34,55,89,144,233....

def fib(n): # write a fibonnaci series upto n
	"""Print Fibonacci series upto n"""
	a, b = 0, 1
	while a < n:
		print a,
		a, b = b, b+a
	

print fib.__doc__ # to print document in quotes
fib(2000)

#: call within this file or from python fibonacci.py
# to call from within python environment:
#>> import fibonacci
#>> fibonacci.fib(2000)
#>>fibonacci.fib.__doc__ # for printing document