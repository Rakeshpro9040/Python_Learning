def askint():
    while True:
        try:
            val = int(input("Please enter an integer: "))
        except ValueError:
            print("Looks like you did not enter an integer!")
            continue
        except:
            print("Some other Error!")
            continue
        else:
            print("Yep that's an integer!")
            break
        finally:
            print("Finally, I executed!")

askint()
"""
Please enter an integer: a
Looks like you did not enter an integer!
Finally, I executed!
Please enter an integer: 1
Yep that's an integer!
Finally, I executed!
"""

