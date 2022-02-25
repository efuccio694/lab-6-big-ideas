import random

name = input("What is your name? ")
secret = random.randint(1,10)

guess = input("Enter an integer between 1 and 10, and I will tell you if your number is the secret...")

try:
    guess = int(guess)
    if secret == guess:
        print("Great job, " + name + " You are correct, the secret number was " + str(secret) )
    else:
        print("Uh-oh! " + name + " were not correct, the secret number was " + str(secret) )
except:
    print("You did not enter a valid integer. Program will now terminate.")
    
        


