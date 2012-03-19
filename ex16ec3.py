#!/usr/bin/python
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do what that, hit RETURN."

raw_input("CHOOSE!")

print "Opening the file...."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

n = '\n'

line1 = "%s%s" % (raw_input('line1: '), n)
line2 = "%s%s" % (raw_input('line2: '), n)
line3 = "%s%s" % (raw_input('line3: '), n)

print "I am going to write these to the file."

target.write('%s%s%s' % (line1, line2, line3))

print "And finally, we close it."
target.close()
