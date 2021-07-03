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
