#!/usr/bin/python
from sys import argv

script, input_file = argv

def print_all(f):
  print f.read()

def rewind(f):
  print f.seek(0)

def print_a_line(line_count, f):
  print line_count, f.readline()

# input_file is the first argument, and it better be a file that python can read
current_file = open(input_file)

print "First let's print the whole file:\n"

# current_file should be the return value of the open method on a file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# current_file should be the return value of the open method on a file
rewind(current_file)

print "Let's print three lines:"

current_line = 1
# current_line is an int, and current_file is a file, which was assigned to
# current_line in line 16 as the return value of the open method
print_a_line(current_line, current_file)

current_line = current_line + 1
# ditto
print_a_line(current_line, current_file)

current_line = current_line + 1
# ditto
print_a_line(current_line, current_file)
