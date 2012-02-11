# x is being set as a variable for a string, with the integer 10 being used for 
# as a string substitute 
x = "There are %d types of people." % 10
# the variable binary is having the string "binary" assigned to it
binary = "binary"
# the variable do_not is having the string "don't" assigned to it
do_not = "don't"
# the variable y is having a string assigned to it, with two instances of string
# substitution, which is getting the substitution variables from a tuple
y = "Thsoe who know %s and those who %s." % (binary, do_not)

# print the variable x
print x
# print the variable y
print y

# print a string, with string substitution with the r operand, which prints whatever
# you give it.
print "I said: %r." % x
# print a string, with string substitution with the s operand, which prints sting
# objects
print "I also said: '%s'." % y

# set the variable hilarious to False (boolean)
hilarious = False
# set the variable joke_evaluation to a string with string substitution with
# the r operand, which prints anything you give it
joke_evaluation = "Isn't that joke so funny?! %r"

# print the variable joke_evaluation (containing a string substitution) with the 
# variable hilarious as the string substitution object
print joke_evaluation % hilarious

# print a simple string
w = "This is the left side of..."
# print another simple string
e = "a string with a right side."

# demonstrate that you can concatenate strings and print them, and show what order
# they will be printed in
print w + e
