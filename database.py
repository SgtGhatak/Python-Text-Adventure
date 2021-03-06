import sqlite3


def Load():
    connect = sqlite3.connect('playerData.db')
    cursor = connect.cursor()
    cursor.execute(
        ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='player' ''')
    if cursor.fetchone()[0] == 1:
        print('Save file found!\n')
        while True:
            x = input('''Would you like to load your save?\n
1. Yes\n
2. No\n\n''')
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
            x = input('''No save file found, do you want to create a new save?\n
1. Yes\n
2. No\n\n''')
            x.lower
            if (x == "yes" or x == "no" or x == "1" or x == "2"):
                break
            else:
                print("Invalid input, please try again\n")
        if(x == "yes" or x == "1"):
            x = ""
            while True:
                playerName = input("What is your character's name?\n")
                x = input('''{} is your characters name?\n
1. Yes\n
2. No\n\n'''.format(playerName))
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
                                mp				integer)
                            ''')
                cursor.execute(
                    "INSERT INTO player VALUES ('1', (?), '10', '10', '10', '10', '10', '10', (?), (?))", (playerName, 10 * 100, 10 * 100,))
                connect.commit()
                connect.close()
                print('Save file created!\n')
                return 1, playerName, 10, 10, 10, 10, 10, 10, 10 * 100, 10 * 100
        else:
            input("Exiting the game.\n")
            exit()


def Save(id, vigor, focus, strength, dexterity, intelligence, faith, hp, mp):
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
            mp = (?)
            WHERE id = (?)''', (vigor, focus, strength, dexterity,
                                intelligence, faith, hp, mp, id))
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
