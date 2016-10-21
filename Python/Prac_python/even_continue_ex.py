# example of continue: also borrowed from C, continues with the next iteration of the loop:

for num in range(2,10):
	if num % 2 == 0:
		print "Found an even no.", num
		continue
	print "Found a number", num
