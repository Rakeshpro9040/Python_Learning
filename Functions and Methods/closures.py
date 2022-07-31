# Without Clusure
def outer_func(msg):

    def inner_func():
        print(msg)
        # here msg variable is called
        # as free variable inside
        # inner function
    
    return inner_func()

outer_func('Hi from without closure') # Hi

# With Closure
def outer_func_clo(msg):

    def inner_func():
        print(msg)
        # here msg variable is called
        # as free variable inside
        # inner function
    
    return inner_func # See the Diff

print(outer_func_clo('Hi'))
# <function outer_func.<locals>.inner_func at 0x00000273939FEF70>
# This is now converted into a Function
print(outer_func_clo('Hi').__name__)
# inner_func

hi_outer_func = outer_func_clo('Hi from closure')
hello_outer_func = outer_func_clo('Hello from closure')

hi_outer_func()
# Hi
hello_outer_func()
# Hello

hi_outer_func()
# Hi
# See here Execution of outer_func_clo
# is done, but hi_outer_func still remembers
# the variable 'Hi'

