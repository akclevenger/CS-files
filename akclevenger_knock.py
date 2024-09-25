print("Amanda Clevenger")
print("Knock Knock joke")
print("8/26/24")


firstName = input("What is your first name?")
print(f"Nice to meet you, {firstName}!")
if firstName == "Andy":
    print("You should do my knock knock joke, it's really funny!")
else:
    print("I don't really like that name but you should go ahead and do my knock knock joke!")
response = input("Would you like to hear a knock knock joke? (Y/N):")
response = response.upper()
if response.startswith("Y"):
    response = input("Knock knock:")
elif response.startswith("N"):
    print("But the joke was really funny, pretty please?")
    response = response.upper()
elif response.startswith("W"):
    response = input("Ash:")
else:
    print("You were suppose to say who's there?")
    response = response.upper()
if response.startswith("A"):
    print("Bless you!!!")
else:
    print("Really? You were suppose to say ash who?") 





  



    
    
    


    






    

 




