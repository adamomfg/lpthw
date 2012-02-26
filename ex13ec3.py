#!/usr/bin/python

from sys import argv

script, first, second, third = argv

fourth = raw_input("Give me another variable, sucker: ")
print "The script is called:", script
print "The first variable is called:", first
print "The second variable is called:", second 
print "The third variable is called:", third 
print "The fourth variable, called from raw_input, is called:", fourth
