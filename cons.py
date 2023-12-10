# Constructors in Python

class Person:
  def __init__(self, name, age, gender):
      self.name = name
      self.age = age
      self.gender = gender

# Creating instances of the Person class
person1 = Person("Alice", 25, "Female")
person2 = Person("Bob", 30, "Male")

# Accessing attributes of the objects
print(f"{person1.name} is {person1.age} years old and is {person1.gender}.")

print(f"{person2.name} is {person2.age} years old and is {person2.gender}.")

print('\n')
# EXMPLE____2

class Miraj:
  def __init__(self,name, age):
    print("This is a person information")
    self.name = name
    self.age = age

  def info(self):
     print(f"{self.name} is {self.age} years old")

a = Miraj("miraj" ,"26")
b = Miraj("sagor","25")
a.info()
b.info()