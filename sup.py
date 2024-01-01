# super keyword in Python
class Parentclass:
  def paratn(self):
    print("This is parent class")

class ChildClass(Parentclass):
  def paratn(self):
    print("MIraj Shahriar")
    super().paratn()
    
  def child(self):
    print("This is a child class")

    super().paratn()

ch_oj= ChildClass()
ch_oj.child()
ch_oj.paratn()


#  Exmple 2:

class Manager:
  def __init__(self, name, id):
    self.name = name
    self.id = id


class Programer(Manager):
  def __init__(self, name, id, language):
    super().__init__(name, id)
    self.language = language

miraj = Manager("Miraj", "19-41734-3")
shahriar  = Programer("Shahriar", "19-3", "Python")
print(miraj.name)
print(miraj.id)

print("\n")

print(shahriar.name)
print(shahriar.id)
print(shahriar.language)
