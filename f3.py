# EXMPLE OF DEFULT FUNCTION
def name(fname, mname= "Jhon" , lname="Whatson"):
  print("Hello" , fname , mname , lname)

name("Amy", "Agarwal" , "jain")

name("Amy", "Agarwal")
name("Amy")
# name("Amy", "Agarwal")
# name("Amy", "Agarwal", "jain")
name("")

# EXMPLE OF KEYWORD FUNCTION
def name(fname, mname= "Jhon" , lname="Whatson"):
  print("Hello" , fname , mname , lname)

# AVERAGE
def average(*numbers):
  sum = 0
  for num in numbers:
    sum = sum +num
  print("Averge number is ", sum/len(numbers))

average(5,6,7,1)
  



