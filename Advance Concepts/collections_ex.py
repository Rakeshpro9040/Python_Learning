import  os
os.system('cls')
from collections import Counter
my_list = [1, 1, 1, 2, 2, 1, 3, 3, 3]
print(Counter(my_list)) # Counter({1: 4, 3: 3, 2: 2})

print('---------------some counter methods----------------')
letters = 'aaaabbbbbbbbbbbbcccddddd'
c = Counter(letters)
print(c)
print(c.most_common())

print('-------------------------------')

from collections import defaultdict
d = defaultdict(lambda: 0)
d['a'] = 1
print(d['a']) # 1
print(d['b']) # 0
print(d) 
# defaultdict(<function <lambda> at 0x00CA7778>, {'a': 1, 'b': 0})

d1 = {'k1':'v1', 'k2':'v2'}
print(d1)

print('----------------namedtuple---------------')
from collections import namedtuple
Student = namedtuple('Student',['name','age','DOB']) 
# Same like declaring object in OOP
S = Student('Nandini','19','2541997')
print(S)
print ("The Student age using index is : ",end ="")  
print (S[1])
#The Student age using index is : 19
print ("The Student name using keyname is : ",end ="")  
print (S.name)
#The Student name using keyname is : Nandini