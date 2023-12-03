# import m

# m.welcome()

# miraj.welcome()

from math import sqrt,pi 
#  in here sqrt is a funtion and pi is the variable...
result = sqrt(9) * pi
print(result)

print("\n")
#  or 

from math import * 

result = sqrt(9) * pi
print(result)

print("\n")

#  or , this called as keyword  

from math import pi ,sqrt as s  

result = s(9) * pi
print(result)

# or , as exmple

import math  as m 

result = m.sqrt(8) * m.pi
print(result)

print("\n")
# dir function 

import math 

print(dir(math))