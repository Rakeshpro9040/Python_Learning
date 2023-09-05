# Keys can not be duplicate, but values can
my_dict = {'key1': 'rakesh', 'key2': 'ramesh'}
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict['key1'])
print(my_dict['key1'].upper())
print(my_dict['key1'].lower())
print('1')

# adv_dictionaries
import os

os.system('cls')

d = {'k1':1, 'k2':2}

# Dictionary comprehension
d1 = {x:x**2 for x in range(10)}
print(d1)

d2 = {x:x**2 for x in range(10)}
print(d1)

# Assign Keys not based on values
print(list(zip(['a','b'], range(2))))

d2 = {x:y**2 for x,y in zip(['a','b'], range(2))}
print(d2)
