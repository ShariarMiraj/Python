# Instance variables vs Class variables in Python 
class Employee:
  def __init__(self,name):
    self.name = name

  def ShowInfo(self):
    print(f"The name of the employee is {self.name}")

emp1 = Employee("MIraj")
emp1.ShowInfo()