import os
import random

os.system('cls')
print('---------randint and seed------------')
print(random.randint(0,100)) # 53, 25, ...
random.seed(101)
print(random.randint(0,100)) # 74
print(random.randint(0,100)) # 24
print(random.randint(0,100)) # 69
print(random.randint(0,100)) # 45
print(random.randint(0,100)) # 59

print('---------list------------')
mylist = list(range(0,10))
print(mylist)
print(random.choice(mylist)) # 0
print(random.choice(mylist)) # 8
# sample with replacement/repetation
print(random.choices(population=mylist, k=5))
# sample without replacement/repetation
print(random.sample(population=mylist, k=5))
# [2, 2, 2, 6, 2]
# [7, 1, 4, 8, 6]
random.shuffle(mylist)
print(mylist)
# [0, 8, 4, 6, 2, 3, 9, 5, 7, 1]
# changes made permanently
print(random.uniform(a=0,b=100))
print(random.gauss(mu=0,sigma=1))
# Uniform distribution
# Gaussian distribution
# 42.23020539303698
# 1.0364470902534306
# Instead use numpy lib