# Inheritance in Python

# Inheritance is a way of creating a new class for using details of an existing class without modifying it.

class Employee:
  def __init__(self,name ,email):
    self.name = name
    self.email = email

  def showInfo(self):
    print(f" Emplpoyee name :{self.name} and this email is: {self.email} ")




class Programer(Employee):
  def showlanguage(self):
    print("This is default language python")



e1 = Employee("miraj" , "miraj@gmail.com")
e1.showInfo()

e2 = Programer("Shahiar" , "doc@gmail.com")
e2.showInfo()
e2.showlanguage()