###Ref:
###[1]:  https://github.com/paulcarroty/Learn-Python-The-Hard-Way/blob/master/ex42.py ;
###[2]:  http://www.blog.pythonlibrary.org/2014/01/21/python-201-what-is-super/

## Animal is- a object (yes, sort of confusing) look at the extra credit
class Animal(object):
pass

## class Dog is-a Animal
class Dog(Animal):

def __init__(self, name):
## class Dog has-a __init__ that takes self and name as parameters
self.name = name

## class Cat is-a Animal
class Cat(Animal):

def __init__(self, name):
## class Cat has-a hat takes self and name as parameters 
self.name = name

## class Person is-a object
class Person(object):

def __init__(self, name):
## class Pearson has-a __init__ that takes parameters self and name
self.name = name

## Person has- a pet of some kind
self.pet = None

## class Employee is-a Pearson
class Employee(Person):

def __init__(self, name, salary):
## ?? hmm what is this strange magic?
##Return a proxy object that delegates to parent or sibling class of type. ;Ref[1],[2]
super(Employee, self).__init__(name)
## Class Employee has a salary attribute
self.salary = salary

## class Fish is-a object
class Fish(object):
pass

## class Salmon is-a Fish
class Salmon(Fish):
pass

## class Halibut is-a Fish
class Halibut(Fish):
pass


## rover is- a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Pearson
mary = Person("Mary")

## pet attribute of mary is-a satan
mary.pet = satan

## frank is a Employee instance
frank = Employee("Frank", 120000)

## pet attribute of frank is a rover
frank.pet = rover

## flipper is-a Fish instance
flipper = Fish()

## crouse is-a Salmon instance
crouse = Salmon()

## harry is-a Halibut instance
harry = Halibut()