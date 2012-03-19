#!/usr/bin/python

from sys import argv

filename = raw_input("What file should I open? ")

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input(" ")

txt_again = open(file_again)

print txt_again.read()
