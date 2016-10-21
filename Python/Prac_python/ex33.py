
numbers = []
inc=2

# while i < 6:
	# print "At the top i is %d" %i
	# numbers.append(i)
	
	# i = i + 1
	# print "Numbers now:",numbers
	# print "At the bottom i is %d" %i
	
# print "The numbers: "

# for num in numbers:
	# print num

def ex33(i,num,inc):
	#i = 0
	while i < num:
	   	print "At the top i is %d" %i
		print "num is %d" %num
		i = i + inc
		numbers.append(i)
	
		
		print "Numbers now:",numbers
		print "At the bottom i is %d" %i
	
	print "The numbers: "

	for num in numbers:
		print num
		
test = range(1,5) #[1,2,3,4]
for n in test:
	print "n is %i" %n
	print "element is %d" %test[n-1] # if test[n]: when n=1, element=2 as n=1 is second index , so we do n-1 to set index as 0 and element as 1 etc.
	i=0
	ex33(i,test[n-1],inc) #or simply ex33(n)

print "All Done!!!"