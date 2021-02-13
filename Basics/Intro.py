# a = 2
# b = 2
# c = 0
# div = '---------'
# list1 = [1, 2, 3, 4, 5, 6]
#
# # Demonstrate IF and FOR
# if a == b and a != 0:
#     print('Yes')
#     for i in range(0, 3):
#         print(i)
#     print(1, div, 1)
#     for i in list1:
#         print(i)
# else:
#     print('No')
#
# print(2, div, 2)
#
# # Demonstrate WHILE
# while c < 10:
#     c += 1
#     if c == 2:
#         # print('c2: ', c)
#         continue
#         # break
#     print('c1: ', c)
# # Not Mandatory
# else:
#     print('All Done')
#
# """
# Let's go deep
# """
# # String Print and comment
# my_str = 'My name is Rakesh. \nPlease find my Contact info below'
# print(my_str)
# print('Here you go!')
# print('\n')
# print('My Last name -' + ' Panigrahi')
# my_str = "Rakesh's Contact +919040735588"
# print(my_str)
# my_str = 'x'
# my_str = my_str*10
# print(my_str)
# my_str = my_str.upper()
# print(my_str)
# my_str = 'my name is z rakesh'
# my_str = my_str.split('z')
# print(my_str)
#
# # Lets see multiple assignment
# a, b = 1, 2
# print(a)
# print(b)
# if a == 1 and b == 3:
#     print('working')
# else:
#     print('not working')
#
# # "Print Formatiing" is another one harldy we use, ex: %s, %d, %f, to restrict datatype
# # Ref - https://www.geeksforgeeks.org/taking-input-in-python/
# a = input("User Input: ")
# print("Output DataType: ", type(a))
# print('Output: %s' %(a))

# Rakesh Practice
# mylist = ['0', '', '']
# print(int(mylist[0]))
# int('')

# def myfunc (mybool):
#     if mybool:
#         return 'Hello'
#     else:
#         return 'Goodbye'
# print(myfunc(True))

# # *args Example
# def myfunc(*args):
#     print(args)
#     return sum(args)
#
# print(myfunc(1,2,3)) # 6 # (1, 2, 3) ## Output is a Tuple
# print(myfunc(1,2,3,4,5,6)) # 21 # (1, 2, 3, 4, 5, 6)

# # **kwargs Example
# def myfunc(**kwargs):
#     print(kwargs)
#     if 'fruit' in kwargs:
#         print('My fruit choice is {}'.format(kwargs['fruit']))
#     else:
#         print('I did not find any fruit here')
#
# myfunc(fruit='apple', veggie='lettuce')
# # {'fruit': 'apple', 'veggie': 'lettuce'}
# # My fruit choice is apple # Output is a Dictionary

# # Mix args Example
# def myfunc(*args,**kwargs):
#     print(args)
#     print(kwargs)
#     print('I would like {} {}'.format(args[0],kwargs['food']))
#
# myfunc(10,20,30,fruit='orange',food='eggs',animal='dog')
# '''
# (10, 20, 30)
# {'fruit': 'orange', 'food': 'eggs', 'animal': 'dog'}
# I would like 10 eggs
# '''

# def myfunc(*args):
#     return [x for x in args if x%2 == 0]
# print(myfunc(1,2,3,10,4,6,7))

# def myfunc(in_str):
#     out_str = ''
#     for (i,x) in enumerate(in_str):
#         if i%2 == 0:
#             out_str+=x.upper()
#         else:
#             out_str+=x.lower()
#     return out_str
#
# print(myfunc('AnthroW'))

# mylist1 = [1, 2, 3]
# mylist2 = [4, 5, 6]
# mylist3 = mylist1 + mylist2
# print(mylist3)
#
# str1 = 'a'
# str2 = 'bc'
# str3 = str1+str2
# print(str3)

# def myfunc(s):
#     print(type(char.upper() if i % 2 else char.lower() for i, char in enumerate(s)))
#     return ''.join(char.upper() if i % 2 else char.lower() for i, char in enumerate(s))
# print(myfunc('AnthroW')) # aNtHrOw

input_string = input('Waiting for Input.. ')
print(input_string)
print(f'{input_string}')