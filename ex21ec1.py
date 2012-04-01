#!/usr/bin/python

def named(first, last):
  name = '%s %s' % (first, last)
  return name

first_name = raw_input('What is your first name? ')
last_name = raw_input('What is your last name? ')

print named(first_name, last_name)
