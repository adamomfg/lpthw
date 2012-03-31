#!/usr/bin/python
# import argv from the sys module
from sys import argv

# assign variables script to argv[0] and input_file to argv[1]
script, input_file = argv

# define a function that takes one argument. the function calls print on the
# results of calling the read method on that file.
# read is a method you can call on files that returns a string
def print_all(f):
  print f.read()

# define a function that takes on argument. the function calls the print method
# on the results of calling the seek method on that file. seek sets the file's
# current position to an offset (0 means absolute file positioning)
def rewind(f):
  print f.seek(0)

# define a function that takes two arguments: an int and a file. the function 
# prints the value of line_count, then prints the contents of that line of 
# the file. somewhat confused as to how it knows to print that particular line,
# as readline() isn't taking an argument, as far as I can tell
def print_a_line(line_count, f):
  print line_count, f.readline()

# assign the variable current_file to the return value of the open method,
# which takes the argument input_file, which was defined above
current_file = open(input_file)

# print statement *yay*
print "First let's print the whole file:\n"

# call the print_all function on the variable current_file, defined above
print_all(current_file)

# print statement
print "Now let's rewind, kind of like a tape."

# call the rewind function on the variable current_file
rewind(current_file)

# print statement
print "Let's print three lines:"

# assign to the value 1 to the variable current_line 
current_line = 1
# call the print_a_line function, taking current_line and current_file arguments
print_a_line(current_line, current_file)

# assign the results of adding 1 to current_line to the variable current_line
current_line = current_line + 1
# call the print_a_line method, taking current_file and current_line argumnets
# (not in that order)
print_a_line(current_line, current_file)

# assign the results of adding 1 to current_line to the variable current_line
current_line = current_line + 1
# call the print_a_line function with the variables current_line and current_file
print_a_line(current_line, current_file)