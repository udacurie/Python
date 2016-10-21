from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL- C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
#target = open(filename, 'w')
target = open(filename, 'r+')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

#print "And finally, we close it."

#target.close()
#........................
print "current pointer position is", target.tell()

pos=target.seek(0,0)
print "moving pointer position to %r" %pos #target.seek(0,0)

print "reading now %r" %target.read()

print "\n current pointer position now is", target.tell()
pos=target.seek(0,0)
print "moving pointer position to %r" %pos #target.seek(0,0)

print "reading again....\n"
print target.read(3)

print "moving pointer position back again to %r" %pos #target.seek(0,0)
pos=target.seek(0,0)

print "reading again but with readlines(1) command...\n"
print target.readlines() 

print "And finally, we close it."

target.close()
#.....................
####can now do the following in command prompt to learn about pointers####
#>>>fobj = open("test.txt")
#>>>fobj. readline(1)
#y
#>>>fobj. readline(2)
#'oo'
#>>> fobj. read()
# 'ooooo\nhoooooooo\nweeeeeeeeee'
#>>>fobj. read(0)
#'' #this is because pointer has reached eof..see more examples below
#>>>fobj. read()
#''
#>>> print fobj.tell() #tell() method indicates current position within file. the next read/write at that many bytes from the beginning of the file.
#32
#>>> print fobj.read()
#
#>>> pos=fobj.seek(0,0) #seek(offset[, from]) method changes the current file position. The offset argument indicates the number of bytes to be moved.the from argument specifies the reference position from where the bytes are to be moved.
#If from is set to 0 :it means use the beginning of the file as the reference position; 1:use the current position as the reference position ; 2: use the end of the file as the reference position.
#>>> print fobj.read()
#yooooooo
#hoooooooo
#weeeeeeeeee
#>>> fobj. readline(7)
#'' # nothing got printed as pointer is again at eof
#>>> fobj. readline(1)
#''
#>>> pos=fobj.seek(0,0)
#>>> fobj. readline(3)
#'yoo'
#>>> fobj. read()
#'ooooo\nhoooooooo\nweeeeeeeeee'
#Note the difference in use for same result:
#>>> pos=fobj.seek(0,0) # reset the pointer to beg of file
#>>> print fobj.read(2)
#yo #compare with below: see no quotes: why?
#>>> pos=fobj.seek(0,0)
#>>> fobj. readline(2) # note same as read(2) ; so read() w/o arg is used to print whole file
#'yo'

# print "And finally, we close it."
# target.close()
