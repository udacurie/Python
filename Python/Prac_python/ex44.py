##Class implicit Inheritance ex: i.e. implicit actions that happen when you define a function in the parent,
##but not in the child.

class Parent(object):

	def implicit(self):
		print "Parent implicit()"
	
class Child(Parent):
	pass
	
mother = Parent()
son = Child()

mother.implicit()
son.implicit()
#op:
#The use of pass under the class Child: is how you tell Python that you want an empty block.
#This creates a class named Child but says that there's nothing new to define in it. Instead it will
#inherit all its behaviour from Parent. When you run this code you get the following:
#Parent.implicit()
#Parent.implicit()

##Class Override Explicitly Inheritance ex:
class Parent(object):

	def override(self):
		print "Parent override()"
		
class Child(Parent):
	
	def override(self):
		print "Child override()"
		
# father = Parent()
# daughter = Child()

# father.override()
# daughter.override()

# The problem with implicitly having functions called is sometimes you want the child to behave
# differently. In this case, you want to override the function in the child, effectively replacing the
# functionality. To do this, just define a function with the same name in Child.
# IMP Note: If the above code is run with 2 classes of same name (Parent, child), Python allows that, as long as 
# they are called by a new instance name : e.g. father and mother instances for Parent classes.
#Giving the output:
# Parent implicit()
# Parent implicit()
# Parent override()
# Child override()
#Giving the output:
# Parent implicit()
# Parent implicit()
# Parent override()
# Child override()

##Note variations: if following instance is re-created:
mother = Parent()
son = Child()
#mother.implicit()
#son.implicit() :
#-> gives following error:
# Parent implicit()
# Parent implicit()
# Traceback (most recent call last):
  # File "ex44.py", line 43, in <module>
    # mother.implicit()
# AttributeError: 'Parent' object has no attribute 'implicit'

mother.override()
son.override()
#However, these calls give the output:
# Parent implicit()
# Parent implicit()
# Parent override()
# Child override()

#BUT if mother.override(), son.override() is called w/o reinstantiating: mother = Parent()
#son = Child(), we get the following error:
# Parent implicit()
# Parent implicit()
# Traceback (most recent call last):
  # File "ex44.py", line 69, in <module>
    # mother.override()
# AttributeError: 'Parent' object has no attribute 'override'


##see e44.py_c for the third example


