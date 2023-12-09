# Map, Filter and Reduce in Python

def cube(x):
  return x * x * x

print(cube(2))

l = [1, 2, 4, 6, 4, 3]

newl = list(map(cube, l))
print(newl)


print('\n')


# Filter()

l = [1, 2, 4, 6, 4, 6]
def filter_function(a):
  return a > 5

newnewl = list(filter(filter_function, l))
print(newnewl)


# .................................................
#  full modifly code 
# same to same uper full code from line (1 - 24)
# Map()
l = [0,1,2,2,2,4]

myf = list(map(lambda x: x*x, l))
print(myf)

print('\n')
# filter
def filter_funcation(b):
  return b>2 or b<2

myfn = list(filter(filter_funcation, l))
print(myfn)

# ................................................

# reduce
from functools import reduce

# Syntax: reduce(function, iterable[, initializer])
numbers = [1, 2, 3, 4, 5]

# {def mysum(x, y):         #this 3 line are same ..(52-54) .when we write the lambda function ..we cant writte this 3 line} 

#   return x + y
# sum = reduce(mysum, numbers)

# Example: Sum all the numbers in the list
sum = reduce(lambda x, y: x + y, numbers)
print(sum)  # Output: 15