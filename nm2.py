# Difference between Python list and aray in NUMpy
import numpy as numpy

l = [1,2,3]
a = numpy.array([1,2,3])

# l.append(4)
# l = l * 2
l = l + [4]
print(l)

# a.append(4)
# a = a * 2
a = a + numpy.array([4])    # Its call Broadcasting method
print(a)