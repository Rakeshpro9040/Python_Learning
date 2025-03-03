import os
import time
import timeit

os.system('cls')

print('-----------Time Elapsed------------')
def func_one(n):
    return list(str(num) for num in range(n))

def func_two(n):
    return list(map(str,range(n)))

start_time = time.time()
func_one(10**5)
end_time = time.time()
elasped_time = end_time - start_time
print(elasped_time)

start_time = time.time()
func_two(10**5)
end_time = time.time()
elasped_time = end_time - start_time
print(elasped_time)

print('-----------timeit------------')
stmt = '''
func_one(100)
'''
setup = '''
def func_one(n):
    return list(str(num) for num in range(n))
'''

print(timeit.timeit(stmt,setup,number=100000))

stmt = '''
func_two(100)
'''
setup = '''
def func_two(n):
    return list(str(num) for num in range(n))
'''

print(timeit.timeit(stmt,setup,number=100000))