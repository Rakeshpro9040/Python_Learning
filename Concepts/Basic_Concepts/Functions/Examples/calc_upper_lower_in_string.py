def up_low(s):
    upper_case_list = [x for x in s if x.isupper()]
    lower_case_list = [x for x in s if x.islower()]
    print(len(upper_case_list))
    print(len(lower_case_list))

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

# y = 'Hh'
# print(y[0].isupper())