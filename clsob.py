# Classes and Objects in Python
class Person:
  name = input("Enter your name:")
  occupation = "software developer"
  univercity ="AIUB"

  def info(self):
    print(f"{self.name} is a {self.occupation} from {self.univercity}")



a=Person()
b=Person()

# b.name="Shahriar"
b.name = input("Enter your name:")
b.occupation="SQA"

a.info()
b.info()
# print(a.name)
# print(a.occupation)
# print(a.univercity)
