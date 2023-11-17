my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
value = my_dict['key1']
value = my_dict.get('key1', 'default_value')
my_dict['key1'] = 'new_value'
my_dict.update({'key1': 'new_value'})
removed_value = my_dict.pop('key1')
print(value)
