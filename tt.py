def fibonacci(n):
  fib_sequence = [0, 1]

  for i in range(2, n):
      next_term = fib_sequence[i-1] + fib_sequence[i-2]
      fib_sequence.append(next_term)

  return fib_sequence

# Change the value of 'n' to control the length of the sequence
n = 10  # You can change this to any positive integer
fib_sequence = fibonacci(n)

print(f"Fibonacci Sequence of length {n}: {fib_sequence}")
