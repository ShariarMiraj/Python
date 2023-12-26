# Instance variable  vs Class variables in Python 
class Employee:
  comapnyName = "Tata"  # Class variables
  # noOfEmployees = 0
  def __init__(self,name):
    self.name = name
    self.amout = 0.2
    # Employee.noOfEmployees +=1

  def ShowInfo(self):
    print(f"The name of the employee is : {self.name} and the amount in {self.comapnyName} is {self.amout}")

  # print(f"The name of the employee is : {self.name} and the amount in {self.noOfEmployees} size{self.comapnyName} is {self.amout}")

emp1 = Employee("MIraj")
emp1.amout =50
emp1.comapnyName = "Google" # Insatance variable
emp1.ShowInfo()
Employee.comapnyName = "Nestle"
print(Employee.comapnyName)

emp2 = Employee("Rohan")
emp2.comapnyName = "cocacola"
emp2.ShowInfo()