a = 2
b = 2
c = 0
div = '---------'
list1 = [1, 2, 3, 4, 5, 6]

if a == b and a != 0:
    print('Yes')
    for i in range(1, 3):
        print(i)
    print(1, div, 1)
    for i in list1:
        print(i)
else:
    print('No')

print(2, div, 2)

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
