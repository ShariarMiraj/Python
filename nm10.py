# (NUMpy) Data science function and Axis

import numpy as np

a = np.array([[7,8,9,10,11,12,13], [17,18,19,20,21,22,23]])
print(a)
print(a.sum)

print(a.sum(axis=0))

# calculated the coulam 
print(a.sum(axis=1))

# calculated the mean
print(a.mean(axis=1))
# calculated the voder all mean 
print(a.mean(axis=None))

# Data science function
print(a.var(axis=1))
print(a.std(axis=None)) # Standard deviation
# or
print(np.std(a, axis=None))

# Minimum and maximum
print(a.min(axis=None))
print(np.max(a, axis=None))