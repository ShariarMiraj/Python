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


# Another code 

def divide_numbers(a, b):
  try:
      result = a / b
      print("Result of division:", result)
  except ZeroDivisionError:
      print("Error: Division by zero is not allowed.")
  except TypeError:
      print("Error: Please provide valid numeric values.")
  except Exception as e:
      print(f"An unexpected error occurred: {e}")
  else:
      print("Division operation completed successfully.")
  finally:
      print("This block always executes, regardless of whether an exception occurred.")

# Example usages
divide_numbers(10, 2)  # Normal case
divide_numbers(5, 0)   # Division by zero
divide_numbers("abc", 2)  # TypeError
