def askint():
    try:
        val = int(input("Please enter an integer: "))
    except:
        print("Looks life you did not enter an integer!")
    finally:
        print("Finally, I executed!")
    print(val)

askint()
print('Done')