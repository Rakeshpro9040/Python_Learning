import os

os.system('cls')
# Arithmetic Operators
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# print(a+b)
# print(a-b)
# print(a*b)

# Division
# print(a/b)
# print(a//b)

# Loops
# n = int(input("Enter n: "))
# for i in range(0,n):
#     print(i**2)

# Write a function
# Leap Year: https://docs.microsoft.com/en-us/office/troubleshoot/excel/determine-a-leap-year
# def is_leap(year):
#     leap = False
#     if (year%400 == 0):
#         return not leap
#     elif (year%4 == 0) and (year%100 != 0):
#         return not leap   
#     else:
#         return leap

# year = int(input("Enter year: "))
# print(is_leap(year))

# Print Function
# n = int(input("Enter a number: "))
# y = ''
# for i in range(1,n+1):
#     y = y+str(i)
# print(y)

# for i in range(1, n+1):
#         print(i, end='')

# List Comprehensions
x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))
n = int(input("Enter n: "))
# mylist = []
# for i in range(0,x+1):
#     for j in range(0,y+1):
#         for k in range(0,z+1):
#             if i+j+k != n:
#                 mylist.append([i,j,k])
# print(mylist)

# mylist = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if (i+j+k) != n]
# print(mylist)