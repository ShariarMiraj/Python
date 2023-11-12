# Recursion in Python
def factorial(num):
  if (num == 0 or num == 1):
    return 1
  else:
    return num * factorial(num - 1)


print(factorial(5))

# Output: 120
# how to work the  series
# 5 * facotiral(4)
# 5 * 4 * facotiral(3)
# 5 * 4 * 3 * facotiral(2)
# 5 * 4 * 3 * 2 * facotiral(1)
# 5 * 4 * 3 * 2 * 1 * facotiral(0)
# 5 * 4 * 3 * 2 * 1 * 1
# 120


# fibonacci in python
def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(3))

print("\n\n")


def print_fibonacci(n):
  if (n <= 0):
    print("Invalid input")
  elif (n == 1):
    print("Fibonacci sequence up to", n, ":")
    print(0)
  else:
    fib = [0, 1]
    for i in range(2, n):
      fib.append(fib[i - 1] + fib[i - 2])
    print("Fibonacci sequence up to", n, ":")
    for i in fib:
      print(i)


# Example usage:
# print_fibonacci(5)
# print(int(input("Enter the valid  number ")))
print_fibonacci(int(input("Enter the valid  number ")))
