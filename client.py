from database import *
from combat import *
from generation_script import *

InitDB()


player_name = input("Enter your name:\n")
chosen_class = 0

while True:
    print("Pick your class\n")
    for i in player_class_input_map:
        print("{}. {}".format(i, player_class_input_map[i]))
    chosen_class = input("\n")

    if chosen_class not in player_class_input_map:
        print("Invalid choice, please choose again.\n")
        continue
    else:
        chosen_class = player_class_input_map[chosen_class]
        break

player = generate_player(player_name, chosen_class)

print("\nWelcome {}, the {}\n".format(player.name, chosen_class))

while True:
    print("Who would you like to fight?\n")
    for i in enemy_map:
        print("{}. {}".format(i, enemy_map[i]))
    chosen_enemy = input("\n")

    if chosen_enemy not in enemy_map:
        print("Invalid choice, please choose again.\n")
        continue
    else:
        chosen_enemy = enemy_map[chosen_enemy]
        break

enemy = generate_enemy(chosen_enemy)

print("\nPrepare yourself " + player.name +
      ", a " + enemy.name + " approaches!\n")

pause()

result = combat_init(player, enemy)

pause()
