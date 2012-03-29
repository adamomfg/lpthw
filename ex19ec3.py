#!/usr/bin/python
def pigLatin(word):
  vowels = ("a", "e", "i", "o", "u", "y")
  if word[0].lower() in vowels or word == "the" or word < 3:
    print word
  elif word[-1] in ('.', ',', '?', '!'):
    print '%s%s' % (word[1:-1], 'ay') 
  else:
    print '%s%s' % (word[1:], 'ay') 

pigLatin('Adam')

pigLatin('derp')

s = 'fuck'
pigLatin(s)

pigLatin('%s' % 'perjorative')

pigLatin('%r' % 3)

sentence = "The quick brown fox jumped over the lazy SRE."
for i in sentence.split(' '):
  pigLatin(i)

sentence_list = ["Do", "I", "really", "have", "to", "type", "this", "shit"]
ss = ' '.join(sentence_list)
for i in ss.split(' '):
  pigLatin(i)
