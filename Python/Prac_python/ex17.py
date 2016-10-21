# from sys import argv
# from os.path import exists

# script, from_file, to_file = argv

# print "Copying from %s to %s" %(from_file, to_file)

# in_file= open(from_file)
# indata = in_file.read()
# doing above in one line
# in_file = open(from_file, 'r',indata) 

# print "The input file is %d bytes long" %len(indata)

# print "Does the output file exists? %r" %exists(to_file)
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input()

# out_file = open(to_file, 'w')
# out_file.write(indata)

# print "Alright, all done"

# out_file.close()
# in_file.close()

#######shorter version of above file##########
from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read(); #now we don't need to do infile.close()
if exists(to_file) == False:
	print "File does not exist: creating new file \n" ;
else:
	print"File already exists: overwriting....\n" ;
	
newfile = open(to_file, 'w').write(indata);

print "length of file copied is %r" %len(indata)

#Note: by putting ; we are maming it into one line of code.
