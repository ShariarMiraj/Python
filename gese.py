# Getters and Setters in Python 

# Getter- a function that returns the value of a private variable
class Myclass:
  def __init__(self,value):
    self._value = value


  def show(self):
    print(f"Value is {self._value}")
  
  @property
  def value(self):
    return  self._value


obj = Myclass(10)
obj.show()
print(obj.value)



# Setter- a function that sets the value of a private variable

class Myclass:
  def __init__(self,value):
    self._value = value

  def show(self):
    print(f"Value is {self._value}")

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, new_value):
    self._value = new_value/10

obj = Myclass(10)
obj.value = 50
obj.show()
    
    
    