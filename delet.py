def factorial(n):
  if n == 0 or n == 1:
      return 1
  else:
      return n * factorial(n - 1)

# Call the function
fact_result = factorial(5)
print("Factorial:", fact_result)


def add_numbers(a, b):
  result = a + b
  return result

# Call the function
sum_result = add_numbers(5, 3)
print("Sum:", sum_result)
