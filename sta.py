# Static Methods in Python 

class MyClass:
  class_variable = "I am a class variable"

  def __init__(self, instance_variable):
      self.instance_variable = instance_variable

  def instance_method(self):
      print(f"I am an instance method. Instance variable: {self.instance_variable}")

  @staticmethod
  def static_method():
      print("I am a static method. No access to instance variables.")

# Creating an instance of MyClass
obj = MyClass(instance_variable="I am an instance variable")

# Accessing instance method
obj.instance_method()

# Accessing static method
MyClass.static_method()
