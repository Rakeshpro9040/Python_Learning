# i_str = 'i am rakesh'
# i_str_1 = i_str.replace(' ', '')
# print(i_str_1)
# # i am ramesh

def palindrome(i_str):
    i_str = i_str.replace(' ', '')
    return i_str == i_str[::-1]

print(palindrome('madam'))

