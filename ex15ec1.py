#!/usr/bin/python

# from the sys module, import the argv module
from sys import argv

# Assign the script and filename variables to argv. argv is a list of 
# command lne parameters passed to a python script, with argv[0] being the 
# script name.
script, filename = argv

# assign the txt variable to the instance of opening the variable filename.
txt = open(filename)

# print the raw contents (read eval print loop!) of the instance of open
# from the variable filename.
print "Here's your file %r:" % filename
# execute the read function on the open instantiation on filename
print txt.read()

# prompt the user of the script for the string representation of the file
# that we had just opened.
print "Type the filename again:"
# assign the variable file_again to the string form of the input from the prompt
file_again = raw_input(" ")

# try to open the file with the name that's the string of the input just
# given to the script. as in, instantiate the open method on the parameter
# file_again, which is a string representation of the file's name
txt_again = open(file_again)

# print the contents of the file that was instantiated with the open command
print txt_again.read()
