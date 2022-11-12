from classes import *
import sqlite3

player_class_input_map = {
    '1': 'Fighter',
    '2': 'Paladin',
    '3': 'Cleric',
}

enemy_map = {
    '1': 'Goblin',
    '2': 'Orc',
    '3': 'Goblin Boss'
}


def generate_player(name, role):
    if(role == "Fighter"):
        player = generate_fighter(name)
    if(role == "Paladin"):
        player = generate_paladin(name)
    if(role == "Cleric"):
        player = generate_cleric(name)

    return player


def generate_fighter(name):
    fighter = Player(0, name, 15, 8, 16, 11, 9, 10)

    fighter.inventory.append(generate_item("Longsword"))
    fighter.inventory.append(generate_item("Chainmail"))

    for i in fighter.inventory:
        if (i.name == "Longsword"):
            fighter.main_hand = i
        if (i.name == "Chainmail"):
            fighter.armour = i
            fighter.ac = int(fighter.armour.prop)

    return fighter


def generate_paladin(name):
    paladin = Player(0, name, 14, 13, 16, 9, 11, 15)

    paladin.inventory.append(generate_item("Greatsword"))
    paladin.inventory.append(generate_item("Chainmail"))

    for i in paladin.inventory:
        if (i.name == "Greatsword"):
            paladin.main_hand = i
        if (i.name == "Chainmail"):
            paladin.armour = i
            paladin.ac = int(paladin.armour.prop)

    return paladin


def generate_cleric(name):
    cleric = Player(0, name, 15, 16, 14, 8, 10, 16)

    cleric.inventory.append(generate_item("Mace"))
    cleric.inventory.append(generate_item("Chainmail"))

    for i in cleric.inventory:
        if (i.name == "Mace"):
            cleric.main_hand = i
        if (i.name == "Chainmail"):
            cleric.armour = i
            cleric.ac = int(cleric.armour.prop)

    return cleric

# fetch item from database and return item object


def generate_item(name):
    connnect = sqlite3.connect('gameDatabase.db')
    cursor = connnect.cursor()

    cursor.execute("SELECT * FROM items WHERE items.name = (?)", (name,))
    item = cursor.fetchone()

    item = Item(item[0], item[1], item[2], item[3], item[4])

    cursor.close()
    return item


# enemy generation

def generate_enemy(name):
    if (name == "Goblin"):
        enemy = generate_goblin()
    if (name == "Orc"):
        enemy = generate_orc()
    if (name == "Goblin Boss"):
        enemy = generate_goblic_boss()
    return enemy


def generate_goblin():
    goblin = Enemy(0, "Goblin", 10, 8, 8, 14, 10, 8, 7, 0, 15, 0.25, "1d6", 0)
    return goblin


def generate_orc():
    orc = Enemy(1, "Orc", 16, 0, 16, 12, 7, 10, 15, 0, 13, 0.5, "1d12", 0)
    return orc


def generate_goblic_boss():
    goblin_boss = Enemy(2, "Goblin Boss", 10, 8, 10,
                        14, 10, 10, 21, 0, 17, 1, "1d6", 2)
    return goblin_boss
