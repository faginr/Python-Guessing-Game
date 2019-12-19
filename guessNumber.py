import random

print("Number Guessing Game")
print("")

# start a loop
flag = True
while flag:
    # user set the max
    num = input("Type your desired number range max (min is 1)")
    # verify input is a number
    if num.isdigit():
        print("Game is Starting...")
        num = int(num)
        # exit loop
        flag = False
    # validation
    else:
        print("Invalid input. Please type a positive number")
# generate answer
answer = random.randint(1,num)

guess = None
count = 1

# game loop
while guess != answer:
    # Collect User input
    guess = input("Guess the number between 1 and " + str(num) + ": ")
    # validate
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Invalid input. Please type a positive number")
        guess = input("Guess the number between 1 and " + str(num) + ": ")
    # win condition
    if guess == answer:
        print ("Correct.")
    # incorrect condition
    else:
        print("Incorrect.")
        count += 1
        # generate hint
        if guess > answer:
            print("The answer is lower.")
        else:
            print("The answer is higher.")
    
print("You guessed " + str(count) + " time(s).")
