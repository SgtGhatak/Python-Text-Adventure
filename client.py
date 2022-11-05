from logging import root
from turtle import onclick, width
from database import *
from classes import *
from combat import *

# # Load data from the database into the player class

# data = Load()
# player = Player(data[0], data[1], data[2], data[3], data[4],
#                 data[5], data[6], data[7], data[8], data[9])

# # Print out the data from the database

# connect = sqlite3.connect('playerData.db')
# cursor = connect.cursor()

# cursor.execute("SELECT * FROM player")
# print(cursor.fetchall())

# connect.commit()
# connect.close()

# player.hp -= 10

# # Save the data from the player class into the database

# Save(player.id, player.vigor, player.focus, player.strength,
#      player.dexterity, player. intelligence, player.faith, player.hp, player.mp)

# # Print out the data from the database

# connect = sqlite3.connect('playerData.db')
# cursor = connect.cursor()

# cursor.execute("SELECT * FROM player")
# print(cursor.fetchall())


# # Commit changes and close
# connect.commit()
# connect.close()
player = Player(0, 'Harken', 10, 10, 10, 10, 10, 10, 10*10, 10*10)
enemy = Enemy(0, 'Goblin', 5, 5, 5, 5, 5, 5, 5)

combat_init(player, enemy)
