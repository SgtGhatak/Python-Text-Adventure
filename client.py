from database import *
from combat import *
from generation_script import *

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
