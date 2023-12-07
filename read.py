# read(), readlines() and other methods | Python
f = open('myf.txt', 'r')
while True:
  line = f.readline()
  if not line:
    break
  print(line)