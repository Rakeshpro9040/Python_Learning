# Stay-Awake Script
# Credit: https://github.com/Johnson468/Stay-Awake
# A small python script to move your mouse, press the shift key, and keep your PC awake when you're away Uses command line arguments to set the number of minutes between movements and requires Python3 or higher. Default timer is 3 minutes, but can be 1 or more.

# Dependencies
# This software uses PyAutoGui https://github.com/asweigart/pyautogui as the driver behind the movement.
# Official Documentation: https://pyautogui.readthedocs.io/en/latest/
# Keyboard Control: https://pyautogui.readthedocs.io/en/latest/keyboard.html
# More Details: https://www.geeksforgeeks.org/mouse-keyboard-automation-using-python/

# Stop Script:- Ctrl-C

import pyautogui
import time
import sys
import os
from datetime import datetime

os.system('cls')
pyautogui.FAILSAFE = False
numMin = None
print(pyautogui.size()) # Size(width=1920, height=1080)
print((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1)
if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    numMin = 1 # Set Timer Here (In Minutes)
else:
    numMin = int(sys.argv[1])
print(numMin)
while(True):
    x=0
    print(f"x1: {x}")
    while(x<numMin):
        print("Sleeping for 1 minute...")
        time.sleep(45) # Set Sleep Timer Here (In Seconds)
        x+=1
        print(f"x2: {x}")
    print("Down Move Started")
    for i in range(0,200):
        pyautogui.moveTo(0,i*4)
    print("Down Move Ended")
    pyautogui.moveTo(1,1)
    print("Back to Initial Position")
    for i in range(0,1):
        # pyautogui.press("shift")
        pass
        print("Shift Clicked")
    print("Movement made at {}".format(datetime.now().time()))
{"mode":"full","isActive":false}