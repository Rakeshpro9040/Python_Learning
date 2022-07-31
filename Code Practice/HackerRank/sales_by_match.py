ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(ar.count(10)) # pair available
print(ar.count(50)//2) # pair not available

print('Method-1')
x = []
for i in ar:
    x.append(ar.count(i)//2)
print(x)
print(set(x))

print('Method-2')
print(sum([ar.count(i)//2 for i in set(ar)]))

print('Method-3')
from collections import Counter
socks, pairs = Counter(ar), 0
print(socks)
for s in socks:
    pairs += socks[s]//2
print(pairs)