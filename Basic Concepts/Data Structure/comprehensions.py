# # Fisrt we will try out using traditional FOR loop
# y = []
# for x in range(0, 3):
#     y.append(x)
# print(y)
#
# # Now we will rewrite this using List Comprehension
# y = [x for x in range(0, 3)]
# print(y)
#
# # Now we will try some complex scenarios
# # Find even number from 1 to 10
# y = [x for x in range(11) if x % 2 == 0]
# print(y)
#
# # Now Lts do some poeration othe o/p
# # square of the o/p even value
# # https://www.includehelp.com/python/calculate-square-of-a-given-number.aspx
# y = [x**2 for x in range(11) if x % 2 == 0]
# print(y)
#
# # Now lets implement nested for loop
# # Find square root of last list result
# z = [int(y**(1/2)) for y in [x**2 for x in range(11) if x % 2 == 0]]
# print(z)
#
# # Now lets check Dictionary comprehension
# my_dict = {'key1': 'rakesh', 'key2': 'ramesh'}
# print(my_dict)
#
# # here we have assigned the value as square of key and key is the evn number between 1 to 10
# my_dict_1 = {key : key**2 for key in range(0,11) if key % 2 == 0}
# print(my_dict_1)
# print('End')

# # convert 'hello' to a list
# word = 'hello'
# mylist = []
#
# # using for loop
# for letter in word:
#     mylist.append(letter)
# print(mylist)
# # ['h', 'e', 'l', 'l', 'o']
#
# # using list comprehensions
# mylist = [letter for letter in word]
# print(mylist)
# # ['h', 'e', 'l', 'l', 'o'

# # Square of all numbers between 0 to 10
# mylist = []
# for i in range(0,11):
#     mylist.append(i**2)
# print(mylist) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
# mylist = [i**2 for i in range(0,11)]
# print(mylist) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Grab only even numebrs
# mylist = [x for x in range(0,11) if x%2==0]
# print(mylist) # [0, 2, 4, 6, 8, 10]

# mylist = [x if x%2==0 else '' for x in range(0,11)]
# print(mylist) # [0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD', 10]
#
# mylist = []
# for x in range(0,11):
#     if x%2==0:
#         mylist.append(x)
#     else:
#         pass
# print(mylist) # [0, 2, 4, 6, 8, 10]

# # Convert celcius temperature to farenheit
# celcius = [0,10,20,30]
# farenheit = [((9/5)*temp+32) for temp in celcius]
# print(farenheit) # [32.0, 50.0, 68.0, 86.0]

# Nested For Loops
mylist = []
for x in [2,4,6]:
    for y in [1,10,1000]:
        mylist.append(x*y)
print(mylist) # [2, 20, 2000, 4, 40, 4000, 6, 60, 6000]

# Using List Comprehensions
mylist = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(mylist) # [2, 20, 2000, 4, 40, 4000, 6, 60, 6000]

x = []
for i in range(1,10):
    x.append(i)
print (x)

x = [i for i in range(0,11,2)]
print (x)