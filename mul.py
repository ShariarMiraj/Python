# Multiple Inheritance in Python 

class Employee:
  def __init__(self, name):
    self.name = name

  def show(self):
    print(f"Name is {self.name}")

class Dancer:
  def __init__(self, dance):
    self.dance = dance

  def show(self):
    print(f"Dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
  def __init__(self, dance, name):
    self.dance = dance
    self.name = name

d = DancerEmployee("Kathak", "Shivani")
print(d.name)
print(d.dance)
d.show()
# print(DancerEmployee.mro())
