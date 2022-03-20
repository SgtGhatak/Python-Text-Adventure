import sqlite3
from classes import *

connect = sqlite3.connect('playerData.db')
cursor = connect.cursor()

player1 = Player('Bob', 100, 20)

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

load = input("Who do you want to load?")

cursor.execute(("SELECT {} FROM player").format(load))
print(cursor.fetchone())

# Commit changes and close
connect.commit()
connect.close()

# connect = sqlite3.connect('playerData.db')
# cursor = connect.cursor()

# rows = cursor.execute("SELECT name, hp, mp").fetchall()
# print(rows)

print("hello world")
