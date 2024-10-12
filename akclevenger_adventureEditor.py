import json
print("Amanda Clevenger")
print("9/30/2024")
print("Text Adventure Editor")
print()
print()




def main():
    game = getDefaultGame()
    keepGoing = True
    while keepGoing:
        userChoice = getUserChoice()
        if userChoice == "0":
            keepGoing = False
        elif userChoice == "1":
            print("Loading default game")
            game = getDefaultGame()
        elif userChoice == "2":
            print("Loading a game file")
            game = loadGame()
        elif userChoice == "3":
            print("Saving current game")
            saveGame(game)
        elif userChoice == "4":
            print("Editing or adding a node")
            editNode()
        elif userChoice == "5":
            print("Playing the current game")
            playGame(game)
        else:
            print("That number does not exist, try again.")
    print()            
            
def getUserChoice():
    print("\n0) Exit")
    print("1) Load default game")
    print("2) Load a game file")
    print("3) Save the current game")
    print("4) Edit or add a node")
    print("5) Play the current game")
    
    return input("What will you do? ")
    
def getDefaultGame():
    return
    
def playGame(game):
    while True:
        print("\n1) Start over")
        print("2) Quit")
        
        choice = input("\nWhich do you choose (1/2): ")
        if choice == "1":
            continue  
        elif choice == "2":
            return
        
nodes = {
    'start': {
        'description': "Do you want to win or lose?",
        'options': {
            'A': {'menu': "I want to win", 'node': 'win'},
            'B': {'menu': "I'd rather lose", 'node': 'lose'}
        }
    },
    'win': {
        'description': "You win!",
        'options': {
            'A': {'menu': "Start over", 'node': 'start'},
            'B': {'menu': "Quit", 'node': 'quit'}
        }
    },
    'lose': {
        'description': "You lose!",
        'options': {
            'A': {'menu': "Start over", 'node': 'start'},
            'B': {'menu': "Quit", 'node': 'quit'}
        }
    },
    'quit': {
        'description': "Thanks for playing. Goodbye!",
        'options': {}
    }
}


def editField(field_name, current_value):
    print(f"\nCurrent {field_name}: {current_value}")
    new_value = input(f"Enter new {field_name}")
    return new_value if new_value else current_value


def editNode():
    print("Current nodes: ")
    print(json.dumps(nodes))
    
    node_name = input("\nChoose node to edit or enter new node name: ")
    
    if node_name in nodes:
        newNode = nodes[node_name].copy()  
        print(f"\nEditing existing node: {node_name}")
    else:
        newNode = {'description': "", 'options': {}}
        print(f"\nCreating new node: {node_name}")
    
    newNode['description'] = editField("description", newNode.get('description', ""))
    
    for option_key in ['A', 'B']:
        menu = newNode['options'].get(option_key, {}).get('menu', "")
        node = newNode['options'].get(option_key, {}).get('node', "")
        
        new_menu = editField(f"Menu {option_key}", menu)
        new_node = editField(f"Node {option_key}", node)
        
        if new_menu or new_node:
            newNode['options'][option_key] = {'menu': new_menu, 'node': new_node}
    return newNode        
        
game_data = {
    "start": {
        "description": "Do you want to win or lose?",
        "options": {
            "A": {"menu": "I want to win", "node": "win"},
            "B": {"menu": "I'd rather lose", "node": "lose"}
        }
    },
    "win": {
        "description": "You win!",
        "options": {
            "A": {"menu": "Start over", "node": "start"},
            "B": {"menu": "Quit", "node": "quit"}
        }
    },
    "lose": {
        "description": "You lose!",
        "options": {
            "A": {"menu": "Start over", "node": "start"},
            "B": {"menu": "Quit", "node": "quit"}
        }
    },
    "quit": {
        "description": "Thanks for playing. Goodbye!",
        "options": {}
    }
}


def loadGame(jsonFile):
    with open(jsonFile, 'w') as file:
        json.dump(game_data, file)  
loadGame('game_data.json')


def saveGame(jsonFile, game_data):
    try:
        with open(jsonFile, 'w') as file:
            json.dump(game_data, file)
    except:
        print(f"Error: Could not save the game to {jsonFile}")

        
            
            
if __name__ == "__main__":
        main() 

