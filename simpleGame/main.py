import os
from entities.character import Character
from entities.weapons import mace, short_bow, iron_sword

hero = Character(name="Hero", health=100)
enemy = Character(name="Enemy", health=100)

while True:

    os.system("cls")
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"{hero.name} health is {hero.health}")
    print(f"{enemy.name} health is {enemy.health}")

    choice = input("[C]ontinue or [E]quip weapon?\n")
    if choice == "E":
        selection = input("Select your weapon: [M]ace, [B]ow or [S]word?\n")
        if selection == "M":
            hero.equip(mace)
        elif selection == "B":
            hero.equip(short_bow)
        elif selection == "S":
            hero.equip(iron_sword)
    elif choice == "C":
        continue

    if hero.health == 0:
        print("Game Over")
        break
    elif enemy.health == 0:
        print("Congratulations, you defeated the enemy.")
        break
