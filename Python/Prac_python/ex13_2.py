from sys import argv

script, first, second, third = argv

fourth = raw_input("enter the 4th arg:")
fifth = raw_input("enter the 5th arg:")
print "\nThe script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fifth variable is:", fifth
print "Your fourth variable is: %s " %fourth

print "this is how you put \n newline"