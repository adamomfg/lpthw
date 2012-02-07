units = raw_input('What unit do you want to convert from? ')
if units.startswith('in'):
  factor = 0.39
  other_unit = 'centimeters'
elif units.startswith('c'):
  factor = 2.54
  other_unit = 'inches'
elif units.startswith('pou') or units.startswith('lbs'):
  factor = 2.20
  other_unit = 'kilos. you drug dealer'
elif units.startswith('kil') or units.startswith('kg'):
  factor = 0.45
  other_unit = 'lbs'

var = int(raw_input('How much have you got? '))

result = factor * var
print 'You have exactly %d %s. Congrats.' % (result, other_unit)
