# # Static Methods in Python
class math:
   @staticmethod
   def add(a,b):
    return a+b

res = math.add(2,3)
print(res)



print("\n")

# Exmple-2

class Math:
  def __init__(self , num):
    self.num = num

  def addtonum(self, num2):
    self.num = self.num + num2

  @staticmethod
  def add(a,b):
    return a+b

a = Math(5)
print(a.num)

a.addtonum(20)
print(a.num)