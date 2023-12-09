# Map, Filter and Reduce in Python

def cube(x):
  return x * x * x

print(cube(2))

l = [1, 2, 4, 6, 4, 3]

newl = list(map(cube, l))
print(newl)