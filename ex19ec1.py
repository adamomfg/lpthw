#!/usr/bin/python
# define a function that takes two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
  # print out the value of cheese_count, which is an int
  print "You have %d cheeses!" % cheese_count
  # print out the value of boxes_of_crackers, which is an int
  print "You have %d boxes of crackers!" % boxes_of_crackers
  # print silly stuff
  print "Man, that's enough for a party!"
  print "Get a blanket.\n"

print "We can just give the function numbers directly:"
# call cheese and crackers with two arguments, which are ints
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# call cheese_and_crackers with two arguments, which are variables for ints
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"

# call cheese_and_crackers with two arguments, also ints,
# but wtih mathematical magic.
cheese_and_crackers(10 + 20, 5 + 6)
