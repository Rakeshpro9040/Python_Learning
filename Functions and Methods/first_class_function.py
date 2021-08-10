# Normal Function Assignment to a Vraible
def square(x):
    return x * x

f = square(5)
print(f) # 25

# Now lets set a Function to a Variable
def square(x):
    return x * x

f = square
print(f(5)) # 25