import sqlite3
from classes import *


def Load():
    connect = sqlite3.connect('playerData.db')
    cursor = connect.cursor()
    cursor.execute(
        ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='player' ''')
    if cursor.fetchone()[0] == 1:
        print('Save file found!\n')
        x = input('Would you like to load your save?\n')
        if (x != 'no'):
            cursor.execute("SELECT * FROM player")
            data = cursor.fetchone()
            return data
        else:
            input("Exiting the game.\n")
            exit()
    else:
        x = input('No save file found, do you want to create a new save?\n')
        x.lower
        if(x != "no"):
            x = ""
            while(x != "yes"):
                playerName = input("What is your character's name?\n")
                x = input("{} is your characters name?\n".format(playerName))
                x.lower

            cursor.execute('''CREATE TABLE player
                            (id		integer		primary key		not null,
                            name			text,
                            vigor			integer,
                            focus			integer,
                            strength		integer,
                            dexterity		integer,
                            intelligence	integer,
                            faith			integer,
                            hp				integer,
                            mp				integer)
                        ''')
            cursor.execute(
                "INSERT INTO player VALUES ('1', (?), '10', '10', '10', '10', '10', '10', (?), (?))", (playerName, 10 * 100, 10 * 100,))
            connect.commit()
            connect.close()
            print('Save file created!\n')
            return 1, playerName, 10, 10, 10, 10, 10, 10
        else:
            input("Exiting the game.\n")
            exit()


def Save(id, vigor, focus, strength, dexterity, intelligence, faith, hp, mp):
    connect = sqlite3.connect('playerData.db')
    cursor = connect.cursor()

    x = input('Would you like to save your data?\n')
    if (x == 'yes'):
        cursor.execute(
            '''UPDATE player
            SET vigor = (?),
            focus = (?),
            strength = (?),
            dexterity = (?),
            intelligence = (?),
            faith = (?),
            hp = (?),
            mp = (?)
            WHERE id = (?)''', (vigor, focus, strength, dexterity, intelligence, faith, hp, mp, id))

    connect.commit()
    connect.close()

    return
