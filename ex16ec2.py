#!/usr/bin/python

from sys import argv

script, filename = argv

txt = open(filename)
print txt.read()

print "Here's your file %r:" % filename

file_again = raw_input("Type the filename again: ")

txt_again = open(file_again)
print txt_again.read()
