# # Problem-1
# try:
#     for i in ['a','b','c']:
#         print(i**2)
# except:
#     print(f"Wrong Integer value!!!")

# # Problem-2
# x = 5
# y = 0
#
# try:
#     z = x/y
# except ZeroDivisionError:
#     print(f'Can not divide by Zero!!!')
# finally:
#     print(f"All Done!")

# Problem-3
def ask():
    while True:
        try:
            x = int(input('Enter a number: '))
        except:
            print(f"Not an Integer")
        else:
            return x**2

print(ask())