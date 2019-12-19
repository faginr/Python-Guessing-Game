#Guess the number game

import random
secretNumber = random.randint(1,100)
print("I am thinking of a number between 1 and 100.")

#Ask for a guess

x = range(1,7,1)
for guessTally in x:
    print("Make a guess:")
    guess = int(input())

    if guess < secretNumber:
        print("Too Low!")
    elif guess > secretNumber:
        print("Too High!")
    else:
        break
#Indentations matter, make sure to indent blocks properly or things will not work!
if guess == secretNumber:
    print("Correct! You guessed correctly in " + str(guessTally) + " guesses.")
else:
    print("Wrong! The number was " + str(secretNumber))
        
