# Exception Handling in Python

b = input("Enter a number: ")
print(f"Multipliction table {b} is :")

try:
  for i in range(1, 11):
    print(f"{int(b)} X {i} = {int(b)*i}")
except:
  print("Invalid number..!")

  
