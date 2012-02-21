#!/usr/bin/python
print "How many pennies do you have?"
pennies = int(raw_input())
print "How many nickels do you have?"
nickels = int(raw_input())
cents = pennies + (nickels * 5)
print "you have %r cents." % cents
