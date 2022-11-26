import random
"""
asks user to input a number 1-10
"""
def get_user_guess():
    return input("Enter a number 1-10\n")

def get_random_number():
    return random.randrange(10)

def compareGuess(guess, random_num):
    if guess > random_num:
        print("too high")

    elif guess < random_num:
        print("too low")

    else:
        print("right on the money")
finalguess = get_user_guess
randomnumber = get_random_number()
print(randomnumber)
print(finalguess)
compareGuess(finalguess, randomnumber)




