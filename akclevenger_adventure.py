print("Amanda Clevenger")
print("Adventure Game")
print("9/24/2024")
getGame = {
    "start": ["You found the entrance to area 51.", "Turn around and head home", "turn", "Start down the path to explore", "explore"],
    "turn": ["You turn around and go home and don't see any cool aliens.", "Start over", "start", "Quit", "quit"],
    "explore": ["You are heading down the path but you see a sign that says danger.", "Continue down the path", "continue", "Take a picture and sneak past the guards", "picture"],
    "continue": ["Military stops you and tells you to turn back now. You lose!", "Start over", "start", "Quit", "quit"],
    "picture": ["You come across a building that has doors and a tunnel next to it.", "Choose the door", "door", "Choose the tunnel", "tunnel"],
    "door": ["You walk in and find strange objects and suits.", "Keep looking around", "look", "There is another tunnel leading to more rooms", "tunnel"],
    "tunnel": ["It's a dead end!", "Start over", "start", "Quit", "quit"],
    "look": ["You start hearing strange noises.", "Investigate the noises", "investigate", "Turn around and leave immediately", "leave"],
    "leave":["You leave and never look back again!", "Start over", "start", "Quit", "quit"],
    "investigate": ["You look further and see aliens!!", "Take a picture and leak it to the world", "world", "Get captured", "captured"],
    "world": ["You become rich and famous from your picture! You win!", "Start over", "start", "Quit", "quit"],
    "captured": ["You're going to prison and possibly be eaten by aliens! You lose!", "Start over", "start", "Quit", "quit"]
}
print()
def getNode(node):
    print(getGame[node][0])
    
    print(f"1. {getGame[node][1]}")
    print(f"2. {getGame[node][3]}")
    
    choice = input("Your choice: (1 or 2): ")
    if choice == "1":
        return getGame[node][2]
    elif choice == "2":
        return getGame[node][4]  
        return node  


def main():
    current_node = "start"
    
    while current_node != "quit":
        current_node = getNode(current_node)

if __name__ == "__main__":
    main()