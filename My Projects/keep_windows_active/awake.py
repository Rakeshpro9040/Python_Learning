''' 
   Stay-Awake Script:
    Credit:- https://github.com/Johnson468/Stay-Awake
    A small python script to move your mouse, press the shift key, 
    and keep your PC awake when you're away Uses command line arguments 
    to set the number of minutes between movements and requires Python3 or higher. 
    Default timer is 3 minutes, but can be 1 or more.
'''

'''
   Dependencies & Docs:
    This software uses PyAutoGui https://github.com/asweigart/pyautogui as the driver behind the movement.
    Official Documentation:- https://pyautogui.readthedocs.io/en/latest/
    Keyboard Control:- https://pyautogui.readthedocs.io/en/latest/keyboard.html
    More Details:- 
        1) https://www.geeksforgeeks.org/mouse-keyboard-automation-using-python/
        2) https://stackabuse.com/getting-started-with-python-pyautogui
'''

'''
   How to Run and Stop:
    Run in Windows CMD
    Navigate to foldewr and open cmd
    Run Python awake.py
    Stop Script:- Ctrl-C
    Find PID:- tasklist /fi "ImageName eq python3.8.exe"
    Kill PID:- taskkill /im python3.8.exe /f
    taskkill /pid 1234 /f
'''

'''
   Main Code:
    print statemets are included for Debugging
'''

'''
   Step-1: Import necessary Python Libraries
'''
import pyautogui
import time
import sys
import os
from datetime import datetime

os.system('cls')
pyautogui.FAILSAFE = False 
# Otherwise once Cursor is reached to corner program will terminate with FailSafeException
numMin = None

'''
   Step-2: Write Logic to Set Timer
'''
# print(pyautogui.size())
# print((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1)
if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    numMin = 3 # Set Timer Here (In Minutes)
else:
    numMin = int(sys.argv[1])
# print(numMin)

'''
   Step-3: Main Loop Logic to Move the Cursor and Click
'''
while(True):
    x=0
    # print(f"x1: {x}")
    while(x<numMin):
        # print("Sleeping for 1 minute...")
        time.sleep(60) # Set Sleep Timer Here (In Seconds)
        x+=1
        # print(f"x2: {x}")
    # print("Down Move Started")
    # for i in range(0,200):
        # pyautogui.moveTo(0,i*4)
    # print("Down Move Ended")
    # pyautogui.moveTo(1,1)
    # print("To Top Left Corner of Screen")
    for i in range(0,3):
        pyautogui.press("shift")
        # pass
        # print("Shift Clicked")
    print("Movement made at {}".format(datetime.now().time()))