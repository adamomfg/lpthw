#!/usr/bin/python

print "the open() function, when called with an argument, will return a file object, using the file() type. So says the man page."

print "the file() function can open a file for reading, writing, or appending, and you pass whatever mode you want as an argument following the argument representing the file name, as in 'r' or whatever. You should probably assign that file to a variable, as in f = file ('~/mystupidfile' 'r'), which would instantiate an object with the properties and methods of that object. i think i've normally used read and readlines, depending on what i wanted to do at the time.\n"

pring "the os() function contains OS routines for Mac, NT, or Posix. this means that there are a bunch of things that can be done to the local operation system through os methods. these include functions for accessing operating system operations like gettign stderror, manipulating files, working with uids, opening pipes to and from a command (returning a file object,) even stuff like nice! you can kill stuff, too, which is always fun. and fork child processes, even. oooh, exec, that would have perhaps helped with the 'no more processes' issue i was having last week." 
