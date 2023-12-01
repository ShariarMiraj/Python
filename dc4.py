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
# my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# # Accessing values
# print("Name:", my_dict['name'])
# print("Age:", my_dict['age'])
# print("City:", my_dict['city'])

# # Adding or updating items
# my_dict['occupation'] = 'Engineer'
# print("Occupation:", my_dict['occupation'])

# # Removing items
# removed_age = my_dict.pop('age')
# print("Removed Age:", removed_age)
# print("Updated Dictionary:", my_dict)

# # Getting values with default
# salary = my_dict.get('salary', 'Not specified')
# print("Salary:", salary)

# # Checking if key exists
# if 'city' in my_dict:
#     print("City exists in the dictionary.")

# # Getting keys and values
# keys = my_dict.keys()
# values = my_dict.values()
# items = my_dict.items()
# print("Keys:", keys)
# print("Values:", values)
# print("Items:", items)

# # Iterating through the dictionary
# print("Iterating through the dictionary:")
# for key, value in my_dict.items():
#     print(f"{key}: {value}")

# # Clearing and copying
# my_dict.clear()
# print("Cleared Dictionary:", my_dict)

# new_dict = my_dict.copy()
# new_dict['new_key'] = 'new_value'
# print("Copied Dictionary:", new_dict)

# Creating a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Dictionary comprehension
squared_values = {key: value**2 for key, value in my_dict.items()}
print("Squared Values:", squared_values)

# Set default value
my_dict.setdefault('occupation', 'Unemployed')
print("Occupation:", my_dict['occupation'])

# Merging dictionaries
additional_info = {'hobbies': ['reading', 'traveling'], 'status': 'Single'}
merged_dict = {**my_dict, **additional_info}
print("Merged Dictionary:", merged_dict)

# Updating values
my_dict.update({'age': 31, 'city': 'San Francisco'})
print("Updated Dictionary:", my_dict)

# Nested dictionaries
nested_dict = {'person': {'name': 'Alice', 'age': 25, 'city': 'Los Angeles'}}
print("Nested Dictionary:", nested_dict['person']['name'])

# Popitem() example
last_item = my_dict.popitem()
print("Last Item Popped:", last_item)
print("Updated Dictionary:", my_dict)

# Dictionary with different key types
mixed_dict = {1: 'one', '2': 'two', (3, 4): 'three-four'}
print("Mixed Dictionary:", mixed_dict)

# Sorting dictionary by keys
sorted_dict = dict(sorted(my_dict.items()))
print("Sorted Dictionary by Keys:", sorted_dict)

