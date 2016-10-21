#Important Note:
##see: https://docs.python.org/2/tutorial/controlflow.html
# The break statement, like in C, breaks out of the smallest enclosing "for" or "while" loop.
# Loop statements may have an else clause; it is executed when the loop terminates through 
# exhaustion of the list (with for) or when the condition becomes false (with while),
# but not when the loop is terminated by a break statement. 
# The else clause below belongs to the for loop, not the if statement


for n in range(2,10):
	print "n = ", n
	for x in range(2,n):
		print "n:", n, " & x:", x
		if n % x == 0:
			#print "entering if loop"
			print n, 'equals', x ,'*', n/x
			break #note the difference in output below w/o break statement; 
				  #note it's breaking of 2nd "for", & not "if" statement
	else:
	#2nd loop fell through (i.e all loop elements exhausted) without finding a factor
	    #print "range(2,n):", range(2,n) 
		print n, 'is a prime number'
		
##Note: range(2,2)= [] ; ranger(2,3)=[2]; range(2,4)= [2,3]	
##O/p without break ##
# 2 is a prime number
# 3 is a prime number
# 4 equals 2 * 2
# 4 is a prime number
# 5 is a prime number
# 6 equals 2 * 3
# 6 equals 3 * 2
# 6 is a prime number
# 7 is a prime number
# 8 equals 2 * 4
# 8 equals 4 * 2
# 8 is a prime number
# 9 equals 3 * 3
# 9 is a prime number

##O/P with break statement###
# 2 is a prime number
# 3 is a prime number
# 4 equals 2 * 2
# 5 is a prime number
# 6 equals 2 * 3
# 7 is a prime number
# 8 equals 2 * 4
# 9 equals 3 * 3
