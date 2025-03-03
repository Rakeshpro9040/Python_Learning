# OLD MACDONALD
# def old_macdonald(name):
#     out = []
#     for i,x in enumerate(name):
#         if i in (0,3):
#             y = x.upper()
#         else:
#             y=x
#         out.append(y)
#     return ''.join(out)
#
# print(old_macdonald('macdonald'))

# # MASTER YODA
# def master_yoda(text):
#     text_list = text.split()
#     text_list.reverse()
#     return ' '.join(text_list)
#
# print(master_yoda('I am home'))
# print(master_yoda('We are ready'))

# # ALMOST THERE
# def almost_there(n):
#     if n in range(100,110):
#         return n in range(100,110)
#     elif n in range(200,2110):
#         return n in range(200,210)
#     else:
#         return False
# print(almost_there(211))