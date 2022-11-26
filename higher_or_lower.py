import random
"""
asks user to input a number 1-10
"""
def get_user_guess():
    num =  input("Enter a number 1-10\n")
    return num

def get_random_number():
    num = random.randrange(10)
    return num

def compareGuess(guess, random):
    result = " "
    if guess > random:
        result = "too high"
    elif guess < random:
        result = "too low"
    else:
        result = "correct guess"
    return result
        
finalguess = int(get_user_guess())
randomnumber = get_random_number()
print("the number is: " + str(randomnumber))
print(compareGuess(finalguess,randomnumber))



    




