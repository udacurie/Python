def add(a,b):
	print "adding %d + %d" %(a,b)
	return a+b
	
def subtract(a,b):
	print "subtracting %d - %d" %(a,b)
	return a-b
	
def multiply(a,b):
	print "multiplying %d * %d" %(a,b)
	return a*b
	
def divide(a,b):
	print "dividing %d / %d" %(a,b)
	return a/b

print "lets do something with these functions!"

age = add(30,5) 
height = subtract(78, 4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq)

#A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight,divide(iq,2))))

print "That becomes:", what, "can you do it by hand?"

# PEMDAS: 
# what = add(35, subtract(74,multiply(180,divide(50,2))))
# = add(35, subtract(74, multiply(180,25)))
# = add(35, subtract(74, 4500))
# =-4391

