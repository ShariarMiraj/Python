# Multidimensional array

import numpy as np


a = np.array([[1,2,3] , [4,5,6]])
b = np.array([[1,2] , [3,4]])
print(a)
print(a.shape)


# print(a[0]) Both are same 9 and 10 number line
print(a[0,:])
print(a.T)       #Transport array



# Calculate inverse of the arrayBy using numpy Linglg  model

print(np.linalg.inv(b))
print(np.linalg.det(b))  #Calculate determinant
print(np.diag(b))        #Calculate diagonal matrix

# Overloaded function to two use cases
c = np.diag(b)
print(np.diag(c))

# Array slicing

d = np.array([[1,2,3,4] , [5,6,7,8]])
print(d)

e = d[0,1:3]
e = d[:,1]
e = d[-1,-1]
e = d[-1,-2]
print(e)

