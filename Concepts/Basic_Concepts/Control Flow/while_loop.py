# x = 0
# while x < 10:
#     print('x is currently: ',x)
#     print(' x is still less than 10, adding 1 to x')
#     x+=1
my_str = 'Sammy'
i = 0
j = len(my_str)
print(j)
while (i < j):
    i+=1
    #print(i)
    if my_str[i-1] == 'z':
        break
    else:
        #continue
        print(my_str[i-1])