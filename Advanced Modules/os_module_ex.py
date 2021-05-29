# f = open('practice.txt', 'w+')
# f.write('This is a test string')
# f.close()

# print('----------------------os----------------')
import os
# print(os.getcwd())
# # C:\Users\rakes\PycharmProjects\Python_Introduction\Advanced Modules
# print(os.listdir())
# # ['collections_ex.py', 'os_module_ex.py', 'practice.txt']
# print(os.listdir('C:\\Users\\rakes\\PycharmProjects\\Python_Introduction\\Advanced Modules'))
# # ['collections_ex.py', 'os_module_ex.py', 'practice.txt']

# print('--------------------shutil----------------')
# import shutil
# shutil.move('practice.txt','C:\\Users\\rakes\\PycharmProjects\\Python_Introduction\\')
# '''
# ----------------------os----------------
# C:\Users\rakes\PycharmProjects\Python_Introduction\Advanced Modules
# ['collections_ex.py', 'os_module_ex.py', 'practice.txt']
# ['collections_ex.py', 'os_module_ex.py', 'practice.txt']
# ----------------------shutil----------------
# '''

print('--------------------send2trash----------------')
import send2trash
send2trash.send2trash('practice.txt')
t1 = os.walk
print(t1)