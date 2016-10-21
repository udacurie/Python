import random
from urllib import urlopen
import sys
import collections

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS =[]

PHRASES = {
	"class %%%(%%%):":
	  "Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)" :
	  "class %%% has-a __init__ that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self, @@@)":
	  "class %%% has-a function named *** that takes self and @@@ parameters.",
	"*** = %%%()":
	  "Set *** to an instance of class %%%.",
	"***.***(@@@)":
	  "From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'":
	  "From *** get the *** attribute and set it to '***'."
 }

#print "\n",PHRASES,"\n","\n"
#print "PHRASES items",PHRASES.items()

PHRASES2 = collections.OrderedDict()
PHRASES2["class %%%(%%%):"] = "Make a class named %%% that is-a %%%."
PHRASES2["class %%%(object):\n\tdef __init__(self, ***)" ] = "class %%% has-a __init__ that takes self and *** parameters.",
PHRASES2["class %%%(object):\n\tdef ***(self, @@@)"] = "class %%% has-a function named *** that takes self and @@@ parameters.",
PHRASES2["*** = %%%()"] = "Set *** to an instance of class %%%."
PHRASES2["***.***(@@@)"] = "From *** get the *** function, and call it with parameters self, @@@."
PHRASES2["***.*** = '***'"] = "From *** get the *** attribute and set it to '***'."
 

# print "\n",PHRASES,"\n","\n"
# for x,y in PHRASES.items():
	# print "entering loop\n"
	# print x, y
	#fis = {x:y}
	#PHRASES2.update(fis)
print "***********************PHRASES2*****************\n"
for x,y in PHRASES2.items():
	#print "PHRASES\n"
	print x, y,"\n"	
#print "\n",PHRASES2,"\n","\n"
print "\n\n"

def convert(snippet, phrase):
	class_names = [w.capitalize() for w in
				   random.sample(WORDS, snippet.count("%%%"))] #creates a list class_names where every element is capitalised
	other_names = random.sample(WORDS, snippet.count("***"))
	results = [] #create an empty list 
	param_names = [] #create an empty list
	
	print "class_names:" %class_names
	print "other_names:" %other_names

#snippets = collections.ordereddict
snippets = PHRASES2.keys()
print "snippets:",snippets
for snippet in snippets:
	phrase = PHRASES2[snippet]
	print "function outcome:",convert(snippet, phrase)

#print "\n",snippets,"\n"
#question, answer = convert(snippet, phrase)