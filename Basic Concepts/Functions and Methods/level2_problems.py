# FIND 33
# def has_33(nums):
#     y = ''
#     for x in nums:
#         if y == x and x == 3:
#             return y == x
#         else:
#             y = x
#     return False

# def has_33(nums):
#     for i in range(0,len(nums)-1):
#         # if nums[i] == 3 and nums[i+1] == 3:
#         #    return True
#         if nums[i:i+2] == [3,3]:
#            return True
#     return False
# print(has_33([1, 3, 3]))
# print(has_33([1, 3, 1, 3]))
# print(has_33([3, 1, 3]))
# print(has_33([3, 1, 3, 3]))

# # PAPER DOLL
# def paper_doll(text):
#     # Using normal for loop
#     # out = ''
#     # for x in text:
#     #     out += (x*3)
#     # return out
#
#     # Using List Comprehension
#     return ''.join([(x*3) for x in text])
#
# print(paper_doll('Hello'))
# print(paper_doll('Mississippi'))

# # BLACKJACK
# def blackjack(a,b,c):
#     x = (a,b,c)
#     y = sum(x)
#     if y <= 21:
#         pass
#     elif (y > 21) and (11 in x):
#         y -= 10
#     else:
#         y = 'BUST'
#     return y
#
# print(blackjack(5,6,7))
# print(blackjack(9,9,10))
# print(blackjack(9,9,11))

# # SUMMER OF '69
# def summer_69(arr):
#     y = False
#     out = []
#     for x in arr:
#         if x == 6:
#             y = True
#         elif (x == 9) and (y == True):
#             y = False
#         elif y:
#             pass
#         else:
#             out.append(x)
#     if y:
#         out = 'WRONG INPUT! 6 must followed by at least one 9!'
#         return (out)
#     else:
#         return sum(out)
#
# print(summer_69([1, 3, 5]))
# print(summer_69([4, 5, 6, 7, 8, 9]))
# print(summer_69([2, 1, 6, 9, 11]))
# print(summer_69([4, 5, 6, 7, 9, 9]))
