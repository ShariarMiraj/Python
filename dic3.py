# # Initializing a dictionary to store Employee IDs
# employee_ids = {'101': 'John Doe', '102': 'Jane Doe', '103': 'Bob Smith'}

# # To check if an employee ID exists
# def check_employee_id(id):
#     return id in employee_ids

# # To get the name of an employee using their ID
# def get_employee_name(id):
#     return employee_ids.get(id, 'Employee ID not found')

# # To add a new employee ID and their name
# def add_employee_id(id, name):
#     employee_ids[id] = name

# # To remove an employee ID
# def remove_employee_id(id):
#     if id in employee_ids:
#         del employee_ids[id]

# # To update the name of an employee
# def update_employee_name(id, name):
#     if id in employee_ids:
#         employee_ids[id] = name

# # Example usage
# print(check_employee_id('101')) # Output: True
# print(get_employee_name('101')) # Output: John Doe

# add_employee_id('104', 'Alice Johnson')
# print(employee_ids) # Output: {'101': 'John Doe', '102': 'Jane Doe', '103': 'Bob Smith', '104': 'Alice Johnson'}

# update_employee_name('101', 'James Doe')
# print(employee_ids) # Output: {'101': 'James Doe', '102': 'Jane Doe', '103': 'Bob Smith', '104': 'Alice Johnson'}

# remove_employee_id('104')
# print(employee_ids) # Output: {'101': 'James Doe', '102': 'Jane Doe', '103': 'Bob Smith'}

# # # Creating a dictionary for employee IDs
# # employee_ids = {'John': 101, 'Jane': 102, 'Bob': 103, 'Alice': 104}

# # # Accessing Values
# # john_id = employee_ids['John']
# # print(f"John's ID: {john_id}")

# # # Adding a new employee
# # employee_ids['Eva'] = 105

# # # Updating an existing employee's ID
# # employee_ids['John'] = 106

# # # Removing an employee by key
# # del employee_ids['Bob']

# # # Removing an employee and getting the value
# # alice_id = employee_ids.pop('Alice')

# # # Checking if a Key Exists
# # if 'Jane' in employee_ids:
# #     print("Jane's ID:", employee_ids['Jane'])

# # # Iterating Over Key-Value Pairs
# # print("\nEmployee IDs:")
# # for name, emp_id in employee_ids.items():
# #     print(f"{name}: {emp_id}")

# # # Getting Keys or Values as Lists
# # names = list(employee_ids.keys())
# # ids = list(employee_ids.values())

# # # Clearing the Dictionary
# # employee_ids.clear()

# # # Printing the final state of the dictionary
# # print("\nEmployee IDs after clearing:", employee_ids)



# Creating a dictionary for employee IDs
employee_ids = {'John': 101, 'Jane': 102, 'Bob': 103, 'Alice': 104}

# Checking if an employee exists
employee_name = 'John'
if employee_name in employee_ids:
    print(f"{employee_name} exists with ID: {employee_ids[employee_name]}")
else:
    print(f"{employee_name} does not exist in the dictionary.")

# Using get() to access a key with a default value
employee_name = 'Charlie'
charlie_id = employee_ids.get(employee_name, 'Not found')
print(f"{employee_name}'s ID: {charlie_id}")

# Updating multiple entries at once
update_data = {'John': 201, 'Eva': 202, 'Charlie': 203}
employee_ids.update(update_data)

# Displaying the updated dictionary
print("\nUpdated Employee IDs:")
for name, emp_id in employee_ids.items():
    print(f"{name}: {emp_id}")
