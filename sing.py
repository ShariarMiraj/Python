# Single Inheritance in Python

# Base class or superclass
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Derived class or subclass
class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks")

# Creating an instance of the Dog class
my_dog = Dog("Buddy")

# Accessing methods from the base class
my_dog.speak()  # Output: Buddy makes a sound

# Accessing methods from the derived class
my_dog.bark()   # Output: Buddy barks
