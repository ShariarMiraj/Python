# Exception Handling in Python

# b = input("Enter a number: ")
# print(f"Multipliction table {b} is :")

# try:
#   for i in range(1, 11):
#     print(f"{int(b)} X {i} = {int(b)*i}")
# except:
#   print("Invalid number..!")


# print("End the program...")


# Syntax Error :

# try:
#   num = int(input("Enter a number: "))

# except ValueError:
#   print("Number the enterd is not an integer")


# Index error :

try:
  num = int(input("Enter a number: "))
  a=[6,3]
  print(a[num])  
except IndexError:
  print("Index out of range")