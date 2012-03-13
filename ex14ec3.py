#!/usr/bin/python
from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "Is python strongly typed?"
answer = raw_input(prompt)
if answer.startswith('y'):
  typed= "strongly"
  response = "You are absolutely incorrect and in for a world of pain."
  judgement = "Idiot."
elif answer.startswith('n'):
  typed= "dynamically"
  response = "You're damn right it's not."
  judgement = "Nice."
else:
  typed = "something stupidly"
  response = "You are unintelligible."
  judgement = "Idiot."

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. 
You think python is %s typed. %s %s
""" % (likes, lives, computer, typed, response, judgement)
