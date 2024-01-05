# Walrus Operator in Python 


print(a:=False)


num = [1,2,3]
while (n:= len(num)) > 0:
  print(num.pop())


# Exmple-2

foods = list()
while True:
  food = input("Enter the food name:")
  if food == "Exit":
    break
  foods.append(food)
print(foods)

# Using the warlus operator in this code 

foods = list()
while (food := input("Enter the food name: ")) !="Exit":
  foods.append(food)
print(foods)