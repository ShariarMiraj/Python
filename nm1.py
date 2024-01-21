import numpy as numpy
print(numpy.__version__)

a = numpy.array([1,2,3])
print(a)
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a.size)
print(a.itemsize)


print(a[0])
a[0] = 10
print(a)

b = a * numpy.array([2,0,2])
print(b)