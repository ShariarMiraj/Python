#2D array in NUMPy

import numpy as np


a = np.array([[1,2] , [3,4] , [5,6]])
print(a)

# Bool Indexing 

bool_idx = a >2
print(bool_idx)
print(a[bool_idx])
# print(a[a>2])     Both are same things line 11 and 12 

b = np.where(a > 2 , a , 2)
print(b)

# Multiple indexing

e = np.array([10,19,30,1,50,61])
print(e)
b = [1,3,5]
print(e[b])

# argwhere funcation
even = np.argwhere(e%2==0).flatten()
print(e[even])