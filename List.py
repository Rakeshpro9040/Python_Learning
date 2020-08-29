my_list = [1, 2, 3, 4, 5, 6]
print(my_list[1])
print(len(my_list))
print(my_list[1:])
print(my_list[:3])
print(my_list[1:3])
dup_list = [1, 2, 3, 4, 5, 6, 6, 7]
print(dup_list)
print(my_list + ['rakesh'])
print(my_list)
my_list = my_list + ['rakesh']
print(my_list)
my_list.append('rocky')
print(my_list)
my_list.pop(0)
print(my_list)
my_list.pop()  # This will pop off last index
print(my_list)
my_list.reverse()
print(my_list)
sort_list = ['a', 'c', 'b']  # Sort will throw error if its mix of numeric and text
#  https://stackoverflow.com/questions/20872314/python-list-sort-query-when-list-contains-different-element-types
sort_list.sort()
print(sort_list)

#  List of List
my_list_1 = [1, 2, 3]
my_list_2 = [5, 6, 4]
my_list_3 = [0, 7, 8]
my_list_4 = [my_list_1, my_list_2, my_list_3]
print(my_list_4)
my_list_3[1] = 9
print(my_list_3)
