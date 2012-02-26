#!/usr/bin/python

print "I tried to run the program with only two arguments, and this is the error I received:\n"
print "Trackback (most recent call last):\n  File \"./ex13.py\", line 5, in <module>\n    script, first, second, third = argv\nValueError: need more than 3 values to unpack.\n"
print "The reason why I got this error is that I did not give enough argv items to \"unpack\" and assign to the variables that I was trying to populate. That's why the error occured on line 5; it would have been fine had I had asked for two variables on that lines, not including the script."
