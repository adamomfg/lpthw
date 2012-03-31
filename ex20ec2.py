#!/usr/bin/python
from sys import argv

script, input_file = argv

def print_all(f):
  print f.read()

def rewind(f):
  print f.seek(0)

# current_line is the first argument used by print_a_line
def print_a_line(line_count, f):
  print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
# current_line is equal to 1
# the first argument to print_a_line is current_line, which becomes assigned to
# the variable line_count (which is internal to print_a_line)
print_a_line(current_line, current_file)

current_line = current_line + 1
# current_line is equal to 2
print_a_line(current_line, current_file)

current_line = current_line + 1
# current_line is equal to 3
print_a_line(current_line, current_file)
