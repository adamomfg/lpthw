#!/usr/bin/python
def add(a, b):
  print "ADDING %d + %d" % (a, b)
  return a + b
  
def subtract(a, b):
  print "SUBTRACTING %d - %d" % (a, b)
  return a - b
  
def multiply(a, b):
  print "MULTIPLYING %d * %d" % (a, b)
  return a * b
  
def divide(a, b):
  print "DIVIDING %d / %d" % (a, b)
  return a / b
  
print "Let's do some math with just functions!"

age = add(30, 5)
height =  subtract(78, 4)
weight = multiply (90, 2)
iq = divide(100, 2)

print age, height, weight, iq

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it anyway
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

print "Divide iq by two, multiply that by weight, subtract that from height, "
"add that to age."

first = iq / 2
second = first * weight
third = height - second
fourth = third + age
print 'The answer is %d.' % fourth

