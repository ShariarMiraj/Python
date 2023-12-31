# Class Methods in Python
class Employee:
   company = " Robi"
   
   def ShowINfo(self,):
       print(f"The Employee name is {self.name} and this company name is {self.company}")

   def ChangeCOmpany(cls, NewnameCOm):
      cls.company = NewnameCOm

e1 = Employee()
e1.name = "MIraj"
e1.ShowINfo()
e1.ChangeCOmpany("Tesla")
e1.ShowINfo()