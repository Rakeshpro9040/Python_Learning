x = set()
print(x)
x.add(1)
print(x)
x.add(2)
print(x)
x.add(1)
print(x)
# Duplicates not allowed

x.add(4)
print(x)
x.add(3)
print(x)

y = {2, 1, 3}
print(y)

my_list = [1, 2, 1, 3, 2, 3]
print(my_list)

# Sort by hashing algorithm
b = hash('ftp')
print(b)
c = hash('sftp')
print(c)

# adv_sets

import os

os.system('cls')

s = set()
s.add(1)
s.add(2)
print(s)
s.clear()
print(s)
s = {1,2,3}
print(s)
sc = s.copy()
print(sc)

# Add/Remove from set
sc.add(4)
s.discard(1)
print(s)

# Difference
print(sc)
print(sc.difference(s)) # sc - s
s1 = {1,2,3}
s2 = {1,4,5}
print("s1-s2")
print(s1.difference(s2))
s1.difference_update(s2) # upadte s = s1 - s2
print(s1)

# Intersection
s1 = {1,2,3}
s2 = {1,2,4}
print(s1.intersection(s2))
s1.intersection_update(s2) # s1 = Intersection
print(s1)

s1 = {1,2}
s2 = {1,2,4}
s3 = {5}
print(s1.isdisjoint(s2)) # Intersection True
print(s1.isdisjoint(s3))

# Sub-set
print(s1.issubset(s2))
print(s2.issuperset(s1))

# Symmetric Diff - Diff bet two sets
print(s1.symmetric_difference(s2))

# Union
print(s1.union(s2))
s1.update(s2) # Updates s1 = s1 U s2
print(s1)