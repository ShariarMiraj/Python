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

