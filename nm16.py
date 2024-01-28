# (NUMpy) Solving function using by linalg

import numpy as np 

a = np.array([[1,1], [1.5,4.0]])
b = np.array([2200,5050])

x =np.linalg.inv(a).dot(b)
print(x)

#  For this we using the solve function cuz its better than inv function

y = np.linalg.solve(a,b)
print(y)






# exple-2
import numpy as np

a = np.array([[1, 1], [1.5, 4.0]])
b = np.array([2200, 5050])

# Solving using np.linalg.solve function
x = np.linalg.solve(a, b)
print(x)
