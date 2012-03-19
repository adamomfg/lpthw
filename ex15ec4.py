#!/usr/bin/python

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
print "Worked as before, but never asked me for input after giving it the name of the file as the first argument."
