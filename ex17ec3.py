#!/usr/bin/python
from sys import argv ; script, from_file, to_file = argv ; indata = open(from_file).read(); output = open(to_file, 'w') ; output.write(indata) ; output.close()
