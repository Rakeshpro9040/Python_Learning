def genfibon(n):
    """
    Generate a fibonnaci sequence up to n
    """
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

for num in genfibon(10):
    print(num)
'''
1 1 2 3 5 8 13 21 34 55
'''

## Normal Function
def fibon(n):
    a = 1
    b = 1
    output = []

    for i in range(n):
        output.append(a)
        a, b = b, a + b

    return output

print(fibon(10)) # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

## next() and iter() built-in functions
# nett()
def simple_gen():
    for x in range(3):
        yield x

g = simple_gen()
print(next(g)) # 0
print(next(g)) # 1
print(next(g)) # 2
print(next(g)) # StopIteration Error

# iter()
s = 'hello'
#Iterate over string
for let in s:
    print(let)

print(next(s)) # TypeError
s_iter = iter(s)
print(next(s_iter)) # h

