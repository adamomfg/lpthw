#!/usr/bin/python
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

horrible_cat = "horrible"

fatter_cat = """
I'll do a list, %s cat wants:
\t* Cat food: %d
\t* Fishies: %r
\t* Catnip\n\t* Grass
"""

print fatter_cat % (horrible_cat, 10, 15) 

fatter_cat = """
I'll do a list, %r cat wants:
\t* Cat food: %d
\t* Fishies: %r
\t* Catnip\n\t* Grass
"""

print fatter_cat % (horrible_cat, 10, 15) 

print "The \%r guy prints up the quotes, so you know it's a string."
