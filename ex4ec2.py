print 'Guido says "C has integers and floating point numbers of various sizes. So, I chose to represent Python integers by a C long (guaranteeing at least 32 bits of precision) and flaoting point numbers by a C double.\n\nhttp://python-history.blogspot.com/2009/03/problem-with-integer-division.html\n'
print 'I am not actually quite sure what this means. What I do know is that when I use a float, I get more precision:'
print 1.0 / 3.0, 'This is 1.0 / 3.0, which is a float, giving me more decimal points.'
print 1 / 3, 'This is 1 / 3, which is an int, rounding down to 0.'
