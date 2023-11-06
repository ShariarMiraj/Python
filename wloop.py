# def count_down(n):
#     while n > 0:
#         print(n)
#         n -= 1

# count_down(5)


user_input = input("Please enter your name: ")
print("Hello, " + user_input + "! Welcome to the world of Python!")


def generate_even_numbers(start, end):
  even_numbers = []
  while start <= end:
      if start % 2 == 0:
          even_numbers.append(start)
      start += 1
  return even_numbers

even_numbers = generate_even_numbers(2, 40)

for number in even_numbers:
  print(number)


print("\n")


def factorial(n):
  if n == 0:
      return 1
  else:
      return n * factorial(n - 1)

try:
  user_input = int(input("Enter a non-negative integer to calculate its factorial: "))
  if user_input < 0:
      print("Please enter a non-negative integer.")
  else:
      result = factorial(user_input)
      print(f"The factorial of {user_input} is {result}")
except ValueError:
  print("Invalid input. Please enter a non-negative integer.")


