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

# Rakesh Practice
mylist = ['0', '', '']
print(int(mylist[0]))
int('')

def myfunc (mybool):
    if mybool:
        return 'Hello'
    else:
        return 'Goodbye'
print(myfunc(True))

def myfunc(in_str):
    out_str = ''
    for (i,x) in enumerate(in_str):
        if i%2 == 0:
            out_str+=x.upper()
        else:
            out_str+=x.lower()
    return out_str

print(myfunc('AnthroW'))

mylist1 = [1, 2, 3]
mylist2 = [4, 5, 6]
mylist3 = mylist1 + mylist2
print(mylist3)

str1 = 'a'
str2 = 'bc'
str3 = str1+str2
print(str3)

def myfunc(s):
    # print(type(char.upper() if i % 2 else char.lower() for i, char in enumerate(s)))
    return ''.join(char.upper() if i % 2 else char.lower() for i, char in enumerate(s))
print(myfunc('AnthroW')) # aNtHrOw

input_string = input('Waiting for Input.. ')
print(input_string)
print(f'{input_string}')

def range_check():
    for i in range(1,10):
        if i == 8:
            return False
        else:
            print(i)

print(range_check())

def fun(x):
    return x*x, x*x*x
print(fun(2))

my_list = [1,2,3,4,5]
print(my_list[::-2])

a,b,c = 1,2,"John"
print(type(c))

class Dummy:
    var=0
d1 = Dummy()
d2 = Dummy()
print(d1)

try:
    print(a)
except NameError:
    print('X')

def f1(x=1,y=2):
    x = x+y
    y += 1
    print(x,y)
f1(y=2,x=1)

for i in enumerate('rakesh'):
    (x,y) = i
    print(x,',',y)

x = "--".join(['a','b','c'])
print(x)

x1 = ['a', 'b', 'c']
x2 = ['x', 'y', 'z']
x3 = list(zip(x1,x2))
print(x3) # [('a', 'x'), ('b', 'y'), ('c', 'z')]
x4 = []
x5 = []
for i,j in x3:
    x4.append(i)
    x5.append(j)
print(x4) # ['a', 'b', 'c']
print(x5) # ['x', 'y', 'z']

from random import shuffle
from random import randint
lst1 = ['a', 'b', 'c', 'd', 'e']
shuffle(lst1)
print(lst1) # ['c', 'a', 'd', 'e', 'b']
randint(0,10) # 9

nm = input('Enter you name: ')
print(nm)

str1 = 'Hello'
print(str1[-5:-1])