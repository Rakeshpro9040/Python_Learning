# Range
# print(list(range(1,11,2)))

# Enumerate
# index_count = 0

# Using normal for loop iteration
# for letter in 'abcde':
#     print("At index {} the letter is {}".format(index_count,letter))
#     print(f'At index {index_count} the letter is {letter}')
#     index_count += 1

# Using enumerate function
for items in enumerate('abcde', start=1):
    print(f'{items}')
# now use Tuples unpacking
for index,letter in enumerate('abcde'):
    print(f'At index {index} the letter is {letter}')