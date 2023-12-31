# dir, __dict__ and help method in Python 


x = [1, 2, 3]
print(dir(x))
print(x.__add__)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age


p = Person("Miraj", 24)
print(p.__dict__)



print(help(Person))