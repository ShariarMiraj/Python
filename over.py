# Method Overriding in Python 

class Shape:
  def __init__(self,x,y):
    self.x = x
    self.y = y

  def area(self):
    return self.x  *  self.y


class Circle(Shape):
  def __init__(self,radius):
    self.radius = radius
    super().__init__(radius,radius)

  def area(self):
    return 3.14 * super().area()


c = Circle(5)
print(c.area())


rec = Shape(3,5)
print(rec.area())




# Exmple 2 from the chatgpt


class Animal:
  def speak(self):
      print("Animal speaks")

class Dog(Animal):
  def speak(self):
      print("Dog barks")

class Cat(Animal):
  def speak(self):
      print("Cat meows")

# Creating instances of the subclasses
dog = Dog()
cat = Cat()

# Calling the overridden methods
dog.speak()  # Output: Dog barks
cat.speak()  # Output: Cat meows
