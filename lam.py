# Lambda functions in Python

add = lambda x, y: x + y
result = add(3, 5)
print(result)  # Output: 8


double = lambda x:  x*x*x
cube = lambda x: x*2
avg = lambda x, y, z: (x + y + z) / 2
print(double(5))
print(cube(5))
print(avg(3, 5, 10))