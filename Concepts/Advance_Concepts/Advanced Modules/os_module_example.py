import os
import shutil
import send2trash
os.system('cls')

print('----------------------Normal open/write----------------')
# f = open('practice.txt', 'w+')
# f.write('This is a test string')
# f.close()

print('----------------------os----------------')
print(os.getcwd())
print(os.listdir())
print(os.listdir('C:\\Users\\rakes\\PycharmProjects\\Python_Introduction\\Advanced Modules'))

print('--------------------shutil----------------')
shutil.move('C:\\Users\\rakes\\PycharmProjects\\Python_Introduction\\practice.txt',
            'C:\\Users\\rakes\\PycharmProjects\\Python_Introduction\\Advanced Modules\\')

print('--------------------send2trash----------------')
# os.unlink('C:\\Users\\rakes\\PycharmProjects\\Python_Introduction\\Advanced Modules\\practice.txt')
# send2trash.send2trash('C:\\Users\\rakes\\PycharmProjects\\Python_Introduction\\Advanced Modules\\practice.txt')
# t1 = os.walk
# print(t1)