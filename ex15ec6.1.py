#!/usr/bin/python

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
for i in txt.readline():
  print i, 'here is another character.'

print "Type the filename again:"
file_again = raw_input(" ")

txt_again = open(file_again)

print txt_again.read()
