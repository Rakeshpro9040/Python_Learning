# # Simple Function call
# def say_hello():
#     print('hello')
# say_hello()

# # Override Function
# def say_hello(name = 'Default'):
#     print(f'Hello {name}')
# say_hello('rakesh')
# say_hello()

# # Using return keyword
# def add_num(num1,num2):
#     return num1+num2
# result = add_num(10,20)
# print(result)

# # Python Dynamic Typing Issue
# def add_num(num1,num2):
#     return num1+num2
# result = add_num(10,20)
# print(result) # 30
# result = add_num('10','20')
# print(result) # 1020
#
# # Functions With Logic
# def even_check(number):
#     return number % 2 == 0
# print(even_check(20))
# print(even_check(21))

# Return True if any number is EVEN inside a List
# def check_even_list(num_list):
#     for number in num_list:
#         if number % 2 == 0:
#             return True # once return hits the function will break there
#         else:
#             # return False # Wrong!!! # due to above reason
#             pass # tells program not to do anything
#     return False # To return False if list does not contain any EVEN number
# print(check_even_list([1,3,5]))
# print(check_even_list([1,34,5]))

# # Return all EVEN numbers in a list
# def check_even_list(num_list):
#     # placeholder variables
#     even_numbers = []
#
#     for number in num_list:
#         if number % 2 == 0:
#             even_numbers.append(number) # store the even numberrs from teh list into another list
#         else:
#             pass
#     return even_numbers
# print(check_even_list([1,3,5]))
# print(check_even_list([1,34,5,4,2]))

# # Tuples unpacking with Python Functions
# work_hours = [('Abby',100), ('Billy',4000), ('Cassie',800)]
# def employee_check(work_hours):
#     current_max = 0
#     employee_of_month = ''
#
#     for employee,hours in work_hours:
#         if hours > current_max:
#             current_max = hours
#             employee_of_month = employee
#         else:
#             pass # in case of 'Cassie' just pass
#
#     # Return
#     return (employee_of_month,current_max)
#
# result = employee_check(work_hours)
# print(result)
