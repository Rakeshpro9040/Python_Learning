# #SPY GAME
# def spy_game(nums):
#     y = False
#     z = ''
#     for x in nums:
#         if (x == 0) or ((x == 0) and (z == '0')):
#             z += str(x)
#         elif (x == 7) and (z == '00'):
#             z += str(x)
#             y = True
#     return y
#
# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,4,5,0]))

# # COUNT PRIMES
# def count_primes(num):
#     cnt = 0
#     for x in range(2,num+1):
#         cnt1 = 0
#         for y in range(1,x+1):
#             if x%y == 0:
#                 cnt1 += 1
#         if cnt1 == 2:
#             cnt += 1
#     return cnt
#
# print(count_primes(100))

def count_primes2(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x%y == 0:
                x += 2
                break
        else: # If the for loop runs without break, then else will be executed
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print(count_primes2(100))

# # PRINT BIG
# def print_big(letter):
#     patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
#     alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4], 'F':[4,9,4,9,9]}
#     for pattern in alphabet[letter.upper()]:
#         print(patterns[pattern])
#
# print_big('b')
#
# print(abs(-7.25)) # 7.25
# a = -7
# b = 7
# print(abs(a-b)) # 14 # To find positive distance between two numbers