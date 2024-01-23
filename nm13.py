# (NUMpy) Generating Array

import numpy as np

a = np.zeros((2,3))
print(a)


a = np.ones((2,3))
print(a)


a = np.full((2,3), 5.0)
print(a)

# Identity matrix
print("\n")
a = np.eye((3))
print(a)

print("\n")
# range method 
a = np.arange(20)
print(a)



print("\n")
# linspace method
a = np.linspace(0,10,5)
print(a)

