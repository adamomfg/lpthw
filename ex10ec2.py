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

print "I'm actually not quite sure why you'd want to use triple single quotes, unless perhaps you wanted to have double quotes in the text. Let's see."

dumb_cat = """
I said, "I am a dumb cat."
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print dumb_cat

print "Nope, I must be dense, because I'm not seeing it. Perhaps just style guide adherence?"
