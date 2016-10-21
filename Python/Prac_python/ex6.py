x = "There are %d types of people. \n" % 10
x1 = "There are {} types of people. \n".format(10)
print x1 == x

binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s. \n" % (binary, do_not)
y1 = "Those who know {} and those who {}. \n".format(binary,do_not)
print y1 == y

print x,x1
print y, y1

print "I said: %r." % x
print "I also said: '%s'." % y

print "I said: {}." .format(x)
print "I said: {}." .format(x1)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e