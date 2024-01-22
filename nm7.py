# Reshaping
import numpy as np


a  = np.arange(1,7)
print(a)
print(a.shape)

b = a.reshape((2,3))
c = a.reshape((3,2))
print(b)
print(c)

d = a[np.newaxis]
e = a[:, np.newaxis]
print(d)
print(d.shape)
print(e.shape)
print(e)
