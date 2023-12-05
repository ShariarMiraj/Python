# Local vs Global Variables in Python

# Local variables are those which are defined inside a function and are only accessible inside that function.

# Global variables are those which are defined outside a function and are accessible inside and outside a function.


x = 4
print(x)

def hello():
  x= 5
  print(f"this is a local variable {x}")
  print("Hellor from miraj...")