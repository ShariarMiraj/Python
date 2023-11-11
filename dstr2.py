class Dog:
  """
  A simple class representing a dog.

  Attributes:
  - name (str): The name of the dog.
  - age (int): The age of the dog in years.

  Methods:
  - bark(): Prints a bark message.
  - birthday(): Increments the age of the dog by 1.
  """

  def __init__(self, name, age):
      """
      Initializes a new instance of the Dog class.

      Parameters:
      - name (str): The name of the dog.
      - age (int): The age of the dog in years.
      """
      self.name = name
      self.age = age

  def bark(self):
      """Prints a bark message."""
      print(f"{self.name} says: Woof! Woof!")

  def birthday(self):
      """Increments the age of the dog by 1."""
      self.age += 1

# Creating an instance of the Dog class
my_dog = Dog("Buddy", 3)

# Using methods of the Dog class
my_dog.bark()
my_dog.birthday()



