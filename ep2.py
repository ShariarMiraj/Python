# Exception Handling in Python with if else 

# try:
#   # Code that may raise an exception
#   x = int(input("Enter a number: "))
#   result = 10 / x
# except ValueError:
#   # Handle the case when the input is not a valid integer
#   print("Invalid input. Please enter a valid number.")
# except ZeroDivisionError:
#   # Handle the case when the user enters 0
#   print("Cannot divide by zero.")
# else:
#   # Code to be executed if no exception is raised
#   print("Result:", result)
# finally:
#   # Code that will be executed no matter what
#   print("Execution complete.")


# exmple - 2 
# try:
#   num =int(input("Enter a number:"))
#   result = 10 / num
# except ValueError:
#   print("Invalid number tpye")

# except ZeroDivisionError:
#   print("Zero cannot be divided any time ")
# else:
#   print("This thee result :", result)

# finally:
#   print("This is the end of the program")


# exmple-3

def divide_Num():
  try:
    a = int(input("Enter the firt number:"))
    b = int(input("Enter the second number:"))
    result = a / b
  except ValueError:
     print("Invalid input")
  except ZeroDivisionError:
      print("Cannot the zero be divi..")
  else:
     print(f" Result:{result:.2f}")

  finally:
     print("End the program..")
divide_Num()

#  Simple finally code :

print("\n")

try:
  l = [1, 5,6,7,8]
  i = int(input("enter the number :"))
  print(l[i])
  
except:
  print("some error is ocured..")

finally:
  print("End the program...")