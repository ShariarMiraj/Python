# (NUMpy)Concatenation

import numpy as np

a = np.array([[1,2] , [3,4]])
print(a)
b = np.array([[5,6]])
c = np.concatenate((a,b))
# c = np.concatenate((a,b) , axis=None)  Flattened D array
print(c)


d = np.concatenate((a,b.T) , axis=1)
print(d)



# hstack and vstack
e = np.array([7,8,9])
f = np.array([10,11,12])

g= np.hstack((e,f))
print(g)
h = np.vstack((e,f))
print(h)

