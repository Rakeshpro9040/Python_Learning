import random

num = random.randint(1,100)

# zero is a good placeholder value. It's useful because it evaluates to "False"
guesses = [0]

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

while True:

    # we can copy the code from above to take an input
    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))

    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue

    # here we compare the player's guess to our number
    if guess == num:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        print('All your guesses are listed below:')
        for i,x in enumerate(guesses):
            print(x)
        break

    # if guess is incorrect, add guess to the list
    guesses.append(guess)

    # when testing the first guess, guesses[-2]==0, which evaluates to False
    # and brings us down to the second section


    if guesses[-2]:  ## This equals to guesses[-2]==0
        # you can use the abs() function to find the positive difference between two numbers
        if abs(num - guess) < abs(num - guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')

    else:
        if abs(num - guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')