##inheritance ("is-a") vs composition ("has-a")
##comment out method 1 (inheritance) before testing method 2(composition)
##See NOTE 3 at the end

# #*********Method 1: 3 Inheritance ways via which Parent-Child classes can interact***************
# # 1. Actions on the child imply an action on the parent.
# # 2. Actions on the child override the action on the parent.
# # 3. Actions on the child alter the action on the parent.
# #************************************************************************************************
# class Parent(object):
	
	# def override(self):
		# print "PARENT override()"
		
	# def implicit(self):
		# print "PARENT  implicit()"
		
	# def altered(self):
		# print "PARENT  altered()"
		
# class Child(Parent):

	# def override(self):
		# print "CHILD override()"
		
	# def altered(self):
		# print "CHILD, BEFORE PARENT altered()"
		# super(Child,self).altered()
		# print "CHILD, AFTER PARENT altered()"
		
# dad = Parent()
# son = Child()

# dad.implicit()
# son.implicit()

# dad.override()
# son.override()

# dad.altered()
# son.altered()

# #o/p:
# # PARENT  implicit()
# # PARENT  implicit()
# # PARENT override()
# # CHILD override()
# # PARENT  altered()
# # CHILD, BEFORE PARENT altered()
# # PARENT  altered()
# # CHILD, AFTER PARENT altered()

# #*********Method 2: Composition*******************************************************************
# Inheritance is useful, but another way to do the exact same thing is just to use other classes and
# modules, rather than rely on implicit inheritance. If you look at the three ways to exploit inheritance,
# two of the three involve writing new code to replace or alter functionality. This can easily
# be replicated by just calling functions in another class.
#NOTE:
#In this code we aren't using the name Parent, since there is not a "parent- child" "is- a" relationship.
#This is a "has- a"" relationship, where Child "has- a" Other that it uses to get its work done.
# #**************************************************************************************************

class Other(object):

	def override(self):
		print "OTHER override()"
		
	def implicit(self):
		print "OTHER implicit()"
		
	def altered(self):
		print "OTHER  altered()"
		
class Child(object): #DIFF 1: "object" passed instead of "OTHER class"
	
	def __init__(self): #DIFF 2: 
		self.other = Other()
		
	def implicit(self):
		self.other.implicit()
		
	def override(self): #Note: even though Other class not directly passed, override still works
		print "CHILD override()"
		
	def altered(self):
		print "CHILD, BEFORE OTHER altered()"
		self.other.altered()#DIFF 4: "SUPER" not used: research further
		print "CHILD, AFTER OTHER altered()"
		
son = Child() #DIFF 3: Due to "has-a" relationship, no need to instantiate Parent()

son.implicit()
son.override()
son.altered()

#o/p"
# OTHER implicit()
# CHILD override()
# CHILD, BEFORE OTHER altered()
# OTHER  altered()
# CHILD, AFTER OTHER altered()
	
	
# NOTE 3: When to Use Inheritance or Composition
# If both solutions solve the problem of reuse, then which one is appropriate in which situations?
# The answer is incredibly subjective, but I’ll give you my three guidelines for when to do which:
# 1. Avoid multiple inheritance at all costs, as it’s too complex to be useful reliably. If you’re
# stuck with it, then be prepared to know the class hierarchy and spend time finding where
# everything is coming from.
# 2. Use composition to package up code into modules that are used in many different unrelated
# places and situations.
# 3. Use inheritance only when there are clearly related reusable pieces of code that fit under
# a single common concept or if you have to because of something you’re using.
# However, do not be a slave to these rules.
	
