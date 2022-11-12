from database import *

from combat import *
from generation_script import *

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

player_class_input_map = {
    '1': 'Fighter',
    '2': 'Cleric',
}

goblin = generate_goblin()

player_name = input("Enter your name:\n")

while True:
    chosen_class = input("Pick your class:\n1. Fighter\n2. Cleric\n")

    if chosen_class not in player_class_input_map:
        print("Invalid choice, please choose again.\n")
        continue
    else:
        chosen_class = player_class_input_map[chosen_class]
        break

player = generate_player(player_name, chosen_class)


print("Prepare yourself " + player.name +
      ", a " + goblin.name + " approachs!\n")

pause()

combat_init(player, goblin)

pause()
