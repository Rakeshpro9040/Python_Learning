import os
import pandas as pd
import numpy as np

os.system('cls')
labels = ['ag','bh','cd']
my_list = [2,3,4]
arr = np.array(my_list)
print(arr)
print(type(arr))
d = {'1':10, 'g':20, 'd':30}

dict1 = {'a':[1,2,3],'b':[4,5,6],'c':[7,8,9],'d':[10,11,12]}
print(pd.DataFrame(dict1))