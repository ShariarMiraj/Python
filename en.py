# Enumerate Function in Python
fruites = [
    "Apple",
    "Banana",
    "Grapes",
]

for index, fruit in enumerate(fruites):

  print(index, fruit)
  if (index == 2):
    print("this is my favert fruits..")

# Emni Example

marks = [95, 96, 97, 98, 99]

for mark in marks:
  print(mark)
  if mark > 90:
    print("Excellent")
  elif mark > 80:
    print("Very Good")
  elif mark > 70:
    print("Good")
  elif mark > 60:
    print("Average")
  else:
    print("Fail")

# Example _2
marks = [95, 96, 97, 98, 99]

index = 0
for mark in marks:
  print(mark)
  if (index == 2):
    print(f"Miraj got this number{index}...")
  index += 1

# or  another way

marks = [95, 96, 97, 98, 99]

index = 0

# for index,  mark in enumerate (marks , start=1):
for index, mark in enumerate(marks):
  print(mark)
  if (index == 3):
    print("Harry is mother fuker =..")

# Em-4
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits, start=1):
  print(f"Index: {index}, Fruit: {fruit}")
