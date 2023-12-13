# Access Modifiers in Python 


# public access modifier

class Employee:
  def __init__(self, name):
    self.name = name

a = Employee("miraj")
print(a.name)

# private access modifier

class Employee2:
  def __init__(self, name):
    self.__name = name

a = Employee2("khan")
# print(a.__name) # cannot be accessed directly
print(a._Employee2__name) # can be accessed indirectly & its called name mangling
print(a.__dir__()) # its help to seee all method in code

# protected access modifier

class Student:
  def __init__(self):
    self._name = "Miraj"

  def _funName(self):
    return "CodeWithMiraj"

class Subject(Student):
  pass

obj = Student()
obj1 = Subject()
print(obj._name)
print(obj._funName())
print(obj1._name)
print(obj1._funName())

