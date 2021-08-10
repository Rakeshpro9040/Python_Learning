# Map Function Example
def square(num):
    return num**2

my_nums = [1,2,3,4,5]
print(map(square,my_nums)) # Stored at this location

for item in map(square,my_nums):
    print(item) # Prints all Items

print(list(map(square,my_nums))) # [1, 4, 9, 16, 25]

# # Filter Function Example
# def check_even(num):
#     return num%2 == 0
#
# my_nums = [1,2,3,4,5,6]
# print(list(filter(check_even,my_nums)))
# # Transform to a list Or Iterate through the results (see below)
# # [2, 4, 6]
#
# for n in filter(check_even,my_nums):
#     print(n) # 2 4 6

# # Lambda Expression Example
# def square(num):
#     result = num ** 2
#     return result
# print(square(3)) # 9

# # Now will convert this into Lambda Expression
# # STEP-1
# def square(num):
#     return num ** 2
# print(square(3)) # 9

# # STEP-2 ## Bad Styling though
# def square(num): return num ** 2
# print(square(3)) # 9

# # STEP-3 # Replace Lambda with keyword def and function name
# square = lambda num: num ** 2
# print(square(3)) # 9

# # Lambda with Map
# my_nums = [1,2,3,4,5]
# print(list(map(lambda num: num**2,my_nums))) # [1, 4, 9, 16, 25]

# # Lambda with Filter
# my_nums = [1,2,3,4,5,6]
# print(list(filter(lambda num: num%2 == 0,my_nums))) # [2, 4, 6]