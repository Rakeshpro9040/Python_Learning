# # LESSER OF TWO EVENS
# def lesser_of_two_evens(a,b):
#     mybool = True
#     for x in (a,b):
#         if x%2 != 0:
#             mybool = False
#     if mybool:
#         return min(a,b)
#     else:
#         return max(a,b)
#
# print(lesser_of_two_evens(2,4))

# # ANIMAL CRACKERS
# def animal_crackers(text):
#     mybool = True
#     y = ''
#     for x in text.split():
#         if x[0] == y:
#             mybool = True
#         else:
#             mybool= False
#         y = x[0]
#     return mybool
#
# print(animal_crackers('Levelheaded Llama Lazy'))
# print(animal_crackers('Crazy Kangaroo'))
# print(animal_crackers('Krazy Kangaroo Citkat'))

# MAKES TWENTY
def makes_twenty(n1,n2):
    mybool = True
    if 20 in (n1,n1):
        return mybool
    elif n1+n2 == 20:
        return mybool
    else:
        return not(mybool)

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))