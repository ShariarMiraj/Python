# Raising custom errors in Python

a = int(input("Enter the number between the 5 or 9"))

if(a<5 or a>9):
  raise ValueError("The number is not between 5 and 9")


salary = int(input("Enter your salary"))
if ( 2000 < salary < 5000):
  raise ValueError("Salary is not between 2000 and 5000") 

