import sqlite3
from classes import *

connect = sqlite3.connect('playerData.db')
cursor = connect.cursor()

player1 = Player('1', 'Bob', 1000, 20)

cursor.execute(
    ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='player' ''')

if cursor.fetchone()[0] == 1:
    print('Save file found!')
else:
    x = input('No save file found, do you want to create a new save?\n')
    x.lower
    if(x != "no"):
        cursor.execute('''CREATE TABLE player
                        (id     integer     primary key     not null,
                        name    text,
                        hp      integer,
                        mp      integer)
                    ''')

        cursor.execute("INSERT INTO player VALUES ('1','Player','100','50')")
        connect.commit()

        print('Save file created!\n')
    else:
        exit()

x = input('update?')
if (x == 'yes'):
    cursor.execute("UPDATE player SET hp = (?) WHERE id=1", (player1.hp,))

cursor.execute("SELECT * FROM player")
data = cursor.fetchone()
print(data)

player2 = Player(data[0], data[1], data[2], data[3])

print("PLAYER 2 " + player2.name, player2.hp, player2.mp)

# # Create table
# cursor.execute('''CREATE TABLE player
#                     (name text,
#                     hp integer,
#                     mp integer)''')

# # Commit changes and close
# connect.commit()
# connect.close()

# Insert data into table
# cursor.execute("INSERT INTO player VALUES ('Player','100','50')")

# save data
# cursor.execute("INSERT INTO player VALUES (:name, :hp, :mp)",
#                {'name': player1.name, 'hp': player1.hp, 'mp': player1.mp})

cursor.execute("SELECT * FROM player")
print(cursor.fetchall())


# Commit changes and close
connect.commit()
connect.close()

# connect = sqlite3.connect('playerData.db')
# cursor = connect.cursor()

# rows = cursor.execute("SELECT name, hp, mp").fetchall()
# print(rows)

print("hello world")
