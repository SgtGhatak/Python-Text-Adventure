from classes import *


def generate_player(name, role):
    if(role == "Fighter"):
        player = generate_fighter(name)
    if(role == "Cleric"):
        player = generate_cleric(name)

    return player


def generate_fighter(name):
    fighter = Player(0, name, 15, 8, 16, 11, 9, 10)

    fighter.inventory.append(shortsword())
    fighter.inventory.append(chainmail())

    for i in fighter.inventory:
        if (i.name == "Shortsword"):
            fighter.main_hand = i
        if (i.name == "Chainmail"):
            fighter.armour = i

    return fighter


def generate_cleric(name):
    cleric = Player(0, name, 15, 16, 14, 8, 10, 16)

    cleric.inventory.append(mace())
    cleric.inventory.append(chainmail())

    for i in cleric.inventory:
        if (i.name == "Mace"):
            cleric.main_hand = i
        if (i.name == "Chainmail"):
            cleric.armour = i

    return cleric


def mace():
    mace = Item("Mace", 1, "Mace", "Weapon")
    return mace


def shortsword():
    shortsword = Item("Shortsword", 1, "Sword", "Weapon")
    return shortsword


def chainmail():
    chainmail = Item("Chainmail", 3, "Medium Armour", "Armour")
    return chainmail


def generate_goblin():
    goblin = Enemy(0, "Goblin", 10, 8, 8, 14, 10, 8, 0.25)
    return goblin
