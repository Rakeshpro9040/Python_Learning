def new_decorator(original_func):
    def wrap_func():
        print("Code would be here, before executing the func")
        original_func()
        print("Code here will execute after the func()")
    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")

# Without Decorator
func_needs_decorator = new_decorator(func_needs_decorator)
# print(func_needs_decorator) # <function new_decorator.<locals>.wrap_func at 0x00EA7220>
func_needs_decorator()
print('-------------------------------------')
"""
Code would be here, before executing the func
This function is in need of a Decorator
Code here will execute after the func()
"""

# With Decorator
@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")
# print(func_needs_decorator) # <function new_decorator.<locals>.wrap_func at 0x015371D8>
func_needs_decorator()
"""
Code would be here, before executing the func
This function is in need of a Decorator
Code here will execute after the func()
"""
