###class example1###
# class MyStuff(object):
		
	# def __init__(self):
		# self.tangerine = "And now a thousand years between" #tangerine variable
	
	# def apple(self):
		# print "I AM CLASSY APPLES!"
#test#
##import test_cl ##can't seem to call a class from another module..why? how to do so?

# thing = MyStuff()
# thing.apple()
# print thing.tangerine

##why don't above two methods work??##

###First Class Exercise###
class Song(object): #Note1: object has to be all lowercase
	
	def __init__(Self, lyrics):
		Self.lyrics = lyrics
		
	def sing_me_a_song(Self):
		for line in Self.lyrics: #self.lyrics ;instance attribute
			print line
			
happy_bday = Song(["Happy birthday to you",
				    "I don't want to get sued",
					"So I'll stop right here"]) #instantiation: creating a mini module and import the class
					
bulls_on_parade = Song(["They rally around the family",
							"With pockets full of shells"])
test_var = ["T'is a new song",
				"Dong Dong Dong"]
print test_var, "=========\n"
new_song = Song(test_var)

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
new_song.sing_me_a_song()


