def count_down(n):
    while n > 0:
        print(n)
        n -= 1

count_down(5)


# Check Even or Odd Function:

def check_even_odd(number):
  if number % 2 == 0:
      return "Even"
  else:
      return "Odd"

# Call the function
num = 7
result = check_even_odd(num)
print(f"{num} is {result}.")

# Call the function
num = 6
result = check_even_odd(num)
print(f"{num} is {result}.")


