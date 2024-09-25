print("Amanda Clevenger")
print("09/10/2024")
print("Number guessing game")
print("")
print("")




import random
correct = 54
number = random.randint(1,100)
tries = 1
max_tries = 7
keepGoing = True
while keepGoing:
    tries += 1
    guess = int(input("What is your guess?:"))
    if guess == correct:
        print("You win!!")
        keepGoing = False
    elif guess <= correct:
        print("Too low!")
    elif guess >= correct:
        print("Too high!")
    if tries >7:
        print("You lose!!")
        keepGoing = False
    
    
