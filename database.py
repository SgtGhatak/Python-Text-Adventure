import sqlite3


def Load():
    connect = sqlite3.connect('playerData.db')
    cursor = connect.cursor()
    cursor.execute(
        ''' SELECT count(name) 
        FROM sqlite_master 
        WHERE type='table' 
        AND name='player' ''')
    if cursor.fetchone()[0] == 1:
        print('Save file found!\n')
        while True:
            print("\U0001F7E9")
            x = input("Would you like to load your save?\n1. Yes\n2. No\n\n")
            x.lower
            if (x == "yes" or x == "no" or x == "1" or x == "2"):
                break
            else:
                print("Invalid input, please try again\n")
        if (x == 'yes' or x == "1"):
            cursor.execute("SELECT * FROM player")
            data = cursor.fetchone()
            return data
        else:
            input("Exiting the game.\n")
            exit()
    else:
        while True:
            x = input(
                "No save file found, do you want to create a new save?\n1. Yes\n2. No\n\n")
            x.lower
            if (x == "yes" or x == "no" or x == "1" or x == "2"):
                break
            else:
                print("Invalid input, please try again\n")
        if(x == "yes" or x == "1"):
            x = ""
            while True:
                playerName = input("What is your character's name?\n")
                x = input(
                    "{} is your characters name?\n1. Yes\n2. No\n\n".format(playerName))
                x.lower
                if (x == "yes" or x == "1"):
                    break
                elif (x == "no" or x == "2"):
                    print("Please enter your name again\n")
                else:
                    print("Invalid input, please try again\n")
            if (x == "yes" or x == "1"):

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
                                mp				integer,
                                inventory       varchar,
                                spells          varchar,
                                main_hand       varchar,
                                off_hand        varchar,
                                armour          varchar)
                            ''')
                connect.commit()
                connect.close()
                print('Save file created!\n')
                return
        else:
            input("Exiting the game.\n")
            exit()


def Save(player):
    connect = sqlite3.connect('playerData.db')
    cursor = connect.cursor()

    while True:
        x = input('''Would you like to save your data?\n
1. Yes\n
2. No\n\n''')
        x.lower
        if (x == "yes" or x == "no" or x == "1" or x == "2"):
            break
        else:
            print("Invalid input, please try again\n")
    if (x == 'yes' or x == "1"):
        cursor.execute(
            '''UPDATE player
            SET vigor = (?),
            focus = (?),
            strength = (?),
            dexterity = (?),
            intelligence = (?),
            faith = (?),
            hp = (?),
            mp = (?),
            inventory = (?),
            spells = (?),
            main_hand = (?),
            off_hand - (?),
            armour = (?),
            WHERE id = (?)''', (player.vigor, player.focus, player.strength, player.dexterity,
                                player.intelligence, player.faith, player.hp, player.mp, id))
    else:
        while True:
            x = input('''Are you sure?\n
                        1. Yes\n
                        2. No\n\n''')
            x.lower
            if (x == "yes" or x == "no" or x == "1" or x == "2"):
                break
            else:
                print("Invalid input, please try again\n")
        if (x == "yes" or x == "1"):
            print("File has not been saved.\n")
            return
        else:
            Save(id, vigor, focus, strength, dexterity,
                 intelligence, faith, hp, mp)
            return

    connect.commit()
    connect.close()

    return
