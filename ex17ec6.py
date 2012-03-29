n = open('derp.txt', 'w')
with open('ex17.txt') as f:
  for line in f:
    n.write(line)
