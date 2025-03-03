def mymodule_func():
    print(f"I am from mymodule.py script")

if __name__ == '__main__':
    print(f'mymodule.py directly called!!!')
    mymodule_func()
else:
    print(f'mymodule.py imported!!!')

