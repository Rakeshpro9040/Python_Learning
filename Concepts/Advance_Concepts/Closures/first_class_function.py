# Normal Function Assignment to a Vraible
def square(x):
    return x * x

f = square(5)
print(f) # 25

# Now lets set a Function to a Variable
def square(x):
    return x * x

f = square # notice that we are not using the () here
print(f(5)) # 25