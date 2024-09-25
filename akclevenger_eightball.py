import random

print("Amanda Clevenger")
print("Magic Eight Ball")
print("9/03/24")
print("")
print("")

print("What will you do?")
print("1: print all the fortunes")
print("2: print a specific fortune")
print("3: get a random fortune")
print("")
fortunes = ["Yes", "No", "Probably not", "Doubtful", "I guess", "Abso-freaking-lutely", "I'm 100% sure of it", "I just don't know"]
answer = input("Please choose 1, 2 or 3:")

        
if answer == '1':
    for index, value in enumerate(fortunes):
        print(f"{index}: {value}")
elif answer == '2':
    response = int(input("What number do you want? (0-7):"))
    for index, value in enumerate(fortunes):
        if index == response:
            print(value)
elif answer == '3':
    num = random.randint(0, 7)
    response = input("Your question:")
    for index, value in enumerate(fortunes):
        if index == num:
            print(value)
else:
    print("Nice try. Please choose a number between 1 and 3.")