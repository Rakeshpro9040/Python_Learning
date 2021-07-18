import os

os.system('cls')
l = [1,2,3]
print(l)
l.append(4)
print(l)
print(l.count(2))
l.append([5,6])
print(l)
l.extend([7,8])
print(l)
print(l.index([5,6]))
l.insert(0,-1)
print(l)
l.pop()
print(l)
l.pop(0)
print(l)
l.remove([5,6])
print(l)
l.append(7)
print(l)
l.remove(7) # Removes 1st Instance
print(l)
l.reverse()
print(l)

