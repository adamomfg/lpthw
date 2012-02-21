#!/usr/bin/python
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %s tall, and %r heavy." % (age, height, weight)
print "When giving back the value, it's in its raw state, and is being printed as a string object, with the surrounding quotes. In that case, the single quote would be processed as closing the beginning single quote."
