# Short hand if else statements 
# a = int(input("Enter the number A :"))
# b=  int(input("Enter the Secondo B :"))
# print("A") if a >b else print("B")

# c = 9 if a>b else 0
# print(c)


# String Concatenation:

is_even = lambda num: "Even" if num % 2 == 0 else "Odd"
print(is_even(7))

# List Comprehension:
numbers = [1, 2, 3, 4, 5]
squared = [x**2 if x % 2 == 0 else x for x in numbers]
print(squared)

# Dictionary Assignment:
age = 25
category = "Young" if age < 30 else "Adult"
print(category)

# Short Circuiting:
value = 15
result = "Valid" if 10 < value < 20 else "Invalid"
print(result)
