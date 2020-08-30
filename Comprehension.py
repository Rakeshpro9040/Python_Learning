# Fisrt we will try out using traditional FOR loop
y = []
for x in range(0, 3):
    y.append(x)
print(y)

# Now we will rewrite this using List Comprehension
y = [x for x in range(0, 3)]
print(y)

# Now we will try some complex scenarios
# Find even number from 1 to 10
y = [x for x in range(11) if x % 2 == 0]
print(y)

# Now Lts do some poeration othe o/p
# square of the o/p even value
# https://www.includehelp.com/python/calculate-square-of-a-given-number.aspx
y = [x**2 for x in range(11) if x % 2 == 0]
print(y)

# Now lets implement nested for loop
# Find square root of last list result
z = [int(y**(1/2)) for y in [x**2 for x in range(11) if x % 2 == 0]]
print(z)

# Now lets check Dictionary comprehension
my_dict = {'key1': 'rakesh', 'key2': 'ramesh'}
print(my_dict)

# here we have assigned the value as square of key and key is the evn number between 1 to 10
my_dict_1 = {key : key**2 for key in range(0,11) if key % 2 == 0}
print(my_dict_1)
print('End')