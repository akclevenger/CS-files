print("Amanda Clevenger")
print("10/20/2024")
print("Turn-based combat system")
print("")
print("")





import random

class Character:
    def __init__(self, name, hitPoints, hitChance, maxDamage, armor):
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor
    
    def fight(self, other):
        if random.randint(1, 100) <= self.hitChance:
            damage = random.randint(1, self.maxDamage)
            absorbed = min(damage, other.armor)  
            final_damage = damage - absorbed
            other.hitPoints -= final_damage
            
            print(f"{self.name} successfully hits {other.name}!")
            print(f"  for {damage} points of damage")
            print(f"  {other.name}'s armor absorbs {absorbed} points")
            print(f"{other.name}: {other.hitPoints} HP\n")
        else:
            print(f"{self.name} misses the attack!\n")
    
    def is_alive(self):
        return self.hitPoints > 0

Dimitri = Character("Dimitri", 20, 75, 6, 3)
Sven = Character("Sven", 15, 50, 8, 1) 

while Dimitri.is_alive() and Sven.is_alive():
    input("Press Enter for another round: ")
    if random.choice([True, False]):
        Dimitri.fight(Sven)
    else:
        Sven.fight(Dimitri)

    if not Sven.is_alive():
        print("Dimitri wins!")
    elif not Dimitri.is_alive():
        print("Sven wins!")