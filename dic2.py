# my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# value = my_dict['key1']
# value = my_dict.get('key1', 'default_value')
# my_dict['key1'] = 'new_value'
# my_dict.update({'key1': 'new_value'})
# removed_value = my_dict.pop('key1')
# # del my_dict['key1']  # Removes the key-value pair with key 'key1'
# # del my_dict         # Deletes the entire dictionary
# if 'key1' in my_dict:
#   print('Key exists!')
#   print(my_dict)

# print(value)


# Creating a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Accessing values
print("Name:", my_dict['name'])
print("Age:", my_dict.get('age', 'N/A'))  # Using get() with a default value

# Updating values
my_dict['age'] = 26

# Adding a new key-value pair
my_dict['gender'] = 'Male'

# Removing a key-value pair
removed_city = my_dict.pop('city')

# Checking if a key exists
if 'city' in my_dict:
    print('City:', my_dict['city'])
else:
    print('City not found.')

# Getting keys, values, and items
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()

print("Keys:", keys)
print("Values:", values)
print("Items:", items)

# Clearing the dictionary
my_dict.clear()

# Printing the dictionary after clearing
print("Dictionary after clearing:", my_dict)
