a = 2
b = 2
c = 0
div = '---------'
list1 = [1, 2, 3, 4, 5, 6]

# Demonstrate IF and FOR
if a == b and a != 0:
    print('Yes')
    for i in range(0, 3):
        print(i)
    print(1, div, 1)
    for i in list1:
        print(i)
else:
    print('No')

print(2, div, 2)

# Demonstrate WHILE
while c < 10:
    c += 1
    if c == 2:
        # print('c2: ', c)
        continue
        # break
    print('c1: ', c)
# Not Mandatory
else:
    print('All Done')

"""
Let's go deep
"""
# String Print and comment
my_str = 'My name is Rakesh. \nPlease find my Contact info below'
print(my_str)
print('Here you go!')
print('\n')
print('My Last name -' + ' Panigrahi')
my_str = "Rakesh's Contact +919040735588"
print(my_str)
my_str = 'x'
my_str = my_str*10
print(my_str)
my_str = my_str.upper()
print(my_str)
my_str = 'my name is z rakesh'
my_str = my_str.split('z')
print(my_str)

# Lets see multiple assignment
a, b = 1, 2
print(a)
print(b)
if a == 1 and b == 3:
    print('working')
else:
    print('not working')

# "Print Formatiing" is another one harldy we use, ex: %s, %d, %f, to restrict datatype
# Ref - https://www.geeksforgeeks.org/taking-input-in-python/
a = input("User Input: ")
print("Output DataType: ", type(a))
print('Output: %s' %(a))