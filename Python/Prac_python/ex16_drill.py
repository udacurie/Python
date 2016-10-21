from sys import argv

script, fname = argv

print "we are going to read file %r" % fname

fobj = open(fname)

print "The file pointer is at: %r \n" %fobj.tell()

print "Here is the whole file: %r \n" %fname

print fobj.read()

print "\n The file pointer is at: %r \n" %fobj.tell()

print "Let us reset the pointer to start \n"

pos = fobj.seek(0,0)

print " The first 5 char of file are: %r \n" %fobj.readline(6)

print "Ok now lets close the file...."

print "closing file..........."
fobj.close()
