# Local vs Global Variables in Python

# Local variables are those which are defined inside a function and are only accessible inside that function.

# Global variables are those which are defined outside a function and are accessible inside and outside a function.


# x = 4  # golbal variable
# print(x)

# def hello():
#   x= 5   # local variable
#   print(f"this is a local variable {x}")
#   print("Hellor from miraj...")

# print(f"this is also  global variable {x} from uper X")
# hello()
# print(f"this is a global variable {x}")


#  Exmple-2

x= 8

def fun():
  global x
  x=9
  y=7
  print(y)
  print(x)

fun()


#  Exmple-3

x= 9

def lop():
  z=11
  print(z)

lop()
print(x)
# print(z) an error cuz this z is a local variable and not a global variable abd is not accessible outside the function