# Map, Filter and Reduce in Python

def cube(x):
  return x * x

print(cube(2))

l = [1, 2, 4, 6, 4, 3]

newl = list(map(cube, l))
print(newl)


print('\n')

from functools import reduce

# Syntax: reduce(function, iterable[, initializer])
numbers = [1, 2, 3, 4, 5]

# Example: Sum all the numbers in the list
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15
