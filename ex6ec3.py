x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# the following line has two strings being put in a string
y = "Thsoe who know %s and those who %s." % (binary, do_not)

print x
print y


# the following line has a string being put in a string
print "I said: %r." % x
# the following line has a string being put in a string
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# well, in this instance, you're printing a string with substitution, and that's 
# the string representation of the boolean value False...
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
