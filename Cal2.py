a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))
if choice == 1:
  print(a + b)
elif choice == 2:
  print(a - b)
elif choice == 3:
  print(a * b)
elif choice == 4:
  print(a / b)
else:
  print("Invalid choice")
