import mymodule
from mymainpackage import mymainpackage_module as mypck_mod
from mymainpackage.mysubpackage import mysubpackage_module as mysubpck_mod

from my_main_package import my_main_package_module as my_pck_mod
from my_main_package.my_sub_package import my_sub_package_module as my_sub_pck_mod

def myprogram_func():
    print(f"I am from myprogram.py script")

mymodule.mymodule_func()

# Normal Directory  --> Without __init__.py script
mypck_mod.mymainpackage_module_func()
mysubpck_mod.mysubpackage_module_func()

# Python Package --> With __init__.py script
my_pck_mod.my_main_package_module_func()
my_sub_pck_mod.my_sub_package_module_func()

if __name__ == '__main__':
    print(f'myprogram.py directly called!!!')
    myprogram_func()
"""
mymodule.py imported!!!
I am from mymodule.py script
I am from mymainpackage_module.py script
I am from mysubpackage_module.py script
I am from my_main_package_module.py script
I am from my_sub_package_module.py script
myprogram.py directly called!!!
I am from myprogram.py script
"""
