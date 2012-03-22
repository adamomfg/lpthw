#!/usr/bin/python
from sys import argv

# assign argv[0] to the variable script, filename variable to argv[1]
script, filename = argv

# a bunch of print statements with string substitution, come on
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do what that, hit RETURN."

# prompt the user for input, with a silly prompt
raw_input("CHOOSE! ")

print "Opening the file...."
# open up the file in write mode (second (optional) argument given)
# truncating will work if the file already exists, says the docs
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
# truncate that shit
target.truncate()

print "Now I'm going to ask you for threre lines."

# assign some variables to raw input from the user
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."

#write the above variables to the file, writing a new line character as well
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
# close the file
target.close()
