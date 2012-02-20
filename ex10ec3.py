#!/usr/bin/python
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

stupid = "cat"
horrible = "\t\t\tI'm a triple tabby %s." % stupid

print horrible

amount = 10
lard_ass_cat_wants = 15

fatter_cat = """
Here's what your dumb cat wants:
"""

print fatter_cat
print "%s wants %r fish and %d fishies." % (stupid, amount, lard_ass_cat_wants)
