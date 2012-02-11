x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Thsoe who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# a longer string (longer than what? the question lacks that detail) is created here as
# the two strings are concatenated, which means mashed together. you know.
print w + e
