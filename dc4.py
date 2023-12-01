# Dictionary Methods in Python

# ep1 = { 122 : 45, 125 : 89}
# ep2 = { 225 : 41, 11112 : 88}
# # ep3 = { 125 : 45, 125 : 89}

# ep1.update(ep2)
# # ep1.pop(125)
# ep1.popitem()
# del ep1[125]
# print(ep1)
# # ep1 = update(ep1, ep3)


# Creating a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing values
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])
print("City:", my_dict['city'])

# Adding or updating items
my_dict['occupation'] = 'Engineer'
print("Occupation:", my_dict['occupation'])

# Removing items
removed_age = my_dict.pop('age')
print("Removed Age:", removed_age)
print("Updated Dictionary:", my_dict)

# Getting values with default
salary = my_dict.get('salary', 'Not specified')
print("Salary:", salary)

# Checking if key exists
if 'city' in my_dict:
    print("City exists in the dictionary.")

# Getting keys and values
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()
print("Keys:", keys)
print("Values:", values)
print("Items:", items)

# Iterating through the dictionary
print("Iterating through the dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")
