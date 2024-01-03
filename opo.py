# Operator Overloading in Python
class victor:
  def __init__(self, i , j, k):
    self.i = i
    self.j = j
    self.k = k

  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"

  def __add__(self, x):
    return victor(self.i + x.i,  self.j+x.j, self.k+x.k)  #addition of two vectors

v1 = victor(3,5,6)
print(v1)

v2 = victor(1,2,9)
print(v2)

print(v1 + v2)