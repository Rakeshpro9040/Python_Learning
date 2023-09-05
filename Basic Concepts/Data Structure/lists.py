# my_list = [1, 2, 3, 4, 5, 6]
# print(my_list[1])
# print(len(my_list))
# print(my_list[1:])
# print(my_list[:3])
# print(my_list[1:3])
# dup_list = [1, 2, 3, 4, 5, 6, 6, 7]
# print(dup_list)
# print(my_list + ['rakesh'])
# print(my_list)
# my_list = my_list + ['rakesh']
# print(my_list)
# my_list.append('rocky')
# print(my_list)
# my_list.pop(0)
# print(my_list)
# my_list.pop()  # This will pop off last index
# print(my_list)
# my_list.reverse()
# print(my_list)
# sort_list = ['a', 'c', 'b']  # Sort will throw error if its mix of numeric and text
# #  https://stackoverflow.com/questions/20872314/python-list-sort-query-when-list-contains-different-element-types
# sort_list.sort()
# print(sort_list)
#
# #  List of List
# my_list_1 = [1, 2, 3]
# my_list_2 = [5, 6, 4]
# my_list_3 = [0, 7, 8]
# my_list_4 = [my_list_1, my_list_2, my_list_3]
# print(my_list_4)
# my_list_3[1] = 9
# print(my_list_3)
#
# # Lets discuss some advenced function
# # append adds the whole object at the end, but extend add the  individual elements at the end.
# my_list_3.append([1, 2])
# print(my_list_3)
#
# my_list_2.extend(['e', 'f'])
# print(my_list_2)
#
# # insert - adds a value in a specific index
# my_list_2.insert(0, 'z')
# print(my_list_2)
#
# # remove - will remove the first occurance of the sepicified value
# my_list_2.remove('e')
# print(my_list_2)

my_list_5 = [1,2,3,4,5]
for i in my_list_5:
    print(i)
# here i is the iterate variable name

# adv_lists

import os

os.system('cls')
l = [1,2,3]
print(l)
l.append(4)
print(l)
print(l.count(2))
l.append([5,6])
print(l)
l.extend([7,8])
print(l)
print(l.index([5,6]))
l.insert(0,-1)
print(l)
l.pop()
print(l)
l.pop(0)
print(l)
l.remove([5,6])
print(l)
l.append(7)
print(l)
l.remove(7) # Removes 1st Instance
print(l)
l.reverse()
print(l)