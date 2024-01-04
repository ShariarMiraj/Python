# Hybrid and Hierarchical Inheritance in Python 

# EXMple-1
class BasaClass:
  pass

class Drived1(BasaClass):
  pass

class Drived2(BasaClass):
  pass

class Drived3(Drived1, Drived2):
  pass

# EXmple -2

# Base class
class Animal1:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Derived classes using multiple inheritance
class Mammal(Animal1):
    def give_birth(self):
        return f"{self.name} gives birth to live young."

class Bird1(Animal1):
    def lay_eggs(self):
        return f"{self.name} lays eggs."

# Derived class using multiple inheritance
class Bat(Mammal, Bird1):
    def fly(self):
        return f"{self.name} can fly using wings."

# Creating an instance of the derived class
bat_instance = Bat("Batwing")

# Calling methods from different base classes
print(bat_instance.speak())        # Output: (inherited from Animal) 
print(bat_instance.give_birth())   # Output: Batwing gives birth to live young.
print(bat_instance.lay_eggs())     # Output: Batwing lays eggs.
print(bat_instance.fly())          # Output: Batwing can fly using wings.









print("\n ")





# Hierarchical Inheritance in Python 

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Derived classes
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Bird(Animal):
    def speak(self):
        return f"{self.name} says Chirp!"

# Creating instances of the derived classes
dog_instance = Dog("Buddy")
cat_instance = Cat("Whiskers")
bird_instance = Bird("Tweetie")

# Calling the speak method on each instance
print(dog_instance.speak())  # Output: Buddy says Woof!
print(cat_instance.speak())  # Output: Whiskers says Meow!
print(bird_instance.speak())  # Output: Tweetie says Chirp!
