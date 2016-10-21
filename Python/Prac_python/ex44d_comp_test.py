class Parent(object):

	def override(self):
		print "PARENT override()"

	def implicit(self):
		print "PARENT implicit()"

	def altered(self):
		print "PARENT altered()"

class Child(object):
		
	def __init__(self):
		self.other = Parent()
	
	def implicit(self):
		self.other.implicit()

	def override(self):
		print "CHILD override()"
		
son = Child()

son.implicit()
son.override()