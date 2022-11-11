import os
import time
# os friendly import so that 'clear' works on widows and linux


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


green_box = '\U0001F7E9'
red_box = '\U0001F7E5'

player_choice_input_map = {
    '1': 'Attack',
    '2': 'Magic',
    '3': 'Item',
    '4': 'Flee'
}

player_flee_input_map = {
    '1': 'Yes',
    '2': 'No'
}


def pause():
    input("Press any key to continue...\n")
    return


"""
initialised the enemy's current HP tracker (as enemy class only holds HP stats) 
then runs the actual combat function.
"""


def combat_init(player, enemy):
    current_enemy_hp = enemy.vigor*10

    combat_result = combat(player, enemy, current_enemy_hp)

    return


"""
The actual combat function.

Runs the combat UI function to display the text GUI to display the player's name 
and hp and the enemy's name and hp.
Then checks the player's and enemy's HP to see if they are dead
    If player is dead, prints out the message saying they're dead and returns -1 
    to indicate player death.
    If enemy is dead, prints out message saying the enemy is dead and returns 1 
    to indicate enemy has died.

Then runs the player choice function, and stores the result, as to run the correct 
function afters once the player has chosen their choice.
    If the player attacks, runs the attack function.
    If the player uses magic, runs the magic function.
    If the player uses an item, runs the item function.
    If the player flees, runs the flee function and returns and exits if the player 
    is successful.

Once the player's choice has been resolves, waits for input, to ensure the user has 
player has read everything and then clears the screen to prevent clutter.

The function is then called recursively again until either the player or enemy
has died or if the player chooses to flee.
"""


def combat(player, enemy, current_enemy_hp):
    combat_ui(player, enemy, current_enemy_hp)

    if (player.checkIfDead() == 1):
        print("The player has died...\n")
        return -1
    elif (current_enemy_hp <= 0):
        print("The enemy is dead!\n")
        return 1

    player_input = player_choices(player)

    if (player_input == 'Attack'):
        current_enemy_hp = player_attack_weapon(
            player, enemy, current_enemy_hp)
    elif (player_input == 'Magic'):
        current_enemy_hp = player_attack_magic(
            player, enemy, current_enemy_hp)
    elif (player_input == 'Item'):
        player_use_item(player)
    elif (player_input == 'Flee'):
        player_flee_choice = player_flee(player)
        if (player_flee_choice == 'Yes'):
            print(player.name + " has successfully fled!\n")
            return 0
        else:
            combat(player, enemy, current_enemy_hp)

    time.sleep(1)
    enemy_action(player, enemy)
    pause()
    cls()
    combat(player, enemy, current_enemy_hp)


"""
Displays the player choices and ensures the player has provided valid input

Prints out a basic text GUI to display the options the player can make.
Ensures the input provided is valid by checking the input to an input mapping
dictionary
"""


def player_choices(player):
    while True:
        print("What would " + player.name + " like to do?\n")
        print("1. Attack     3. Item\n")
        print("2. Magic      4. Flee\n")
        player_input = str(input().lower())
        print("\n")

        if player_input not in player_choice_input_map:
            print("Invalid choice, please choose again.\n")
            continue
        else:
            player_input = player_choice_input_map[player_input]
            return player_input


"""
Displays the text based combat GUI

Overall function is to display the names, hps and sets of unicode characters
to represent the hp bars of both the enemy and the player.

Calculates the maximum hp of the player and enemy using their stats and the
size that each "box" or unicode character should represent. The maximum amount 
of boxes that should be displayed is calculated off the maximum hp and the size
of the boxes. The hp boxes that should be shown are then calculated by multiplying
the current hp by the box size, which stores the appropriate amount of unicode
characters into the respect variable. The remaining blank boxes are then calculated
after by subtracting the maximum amount of boxes by the stores boxes that represents
the current hp. This is then multiplayed by a blank character and stored, as to fill
in the blanks for the missing HP

After the calculations are done, a basic text GUI is printed out using the stored
variables, with the enemy's details being printed on top and the player's details
being printed at the bottom of the GUI
"""


def combat_ui(player, enemy, current_enemy_hp):
    # player's calculations
    max_player_hp = player.vigor*10
    player_hp_box = (player.vigor*10)/10

    player_boxes = int(max_player_hp/player_hp_box)
    current_player_boxes = int(player.hp/player_hp_box)
    player_remaining_hp = player_boxes - current_player_boxes

    player_hp_display = green_box * current_player_boxes
    player_remaining_hp_display = ' ' * player_remaining_hp

    # enemy's calculations
    max_enemy_hp = enemy.vigor*10
    enemy_hp_box = (enemy.vigor*10)/10

    enemy_boxes = int(max_enemy_hp/enemy_hp_box)
    current_enemy_boxes = int(current_enemy_hp/enemy_hp_box)
    enemy_remaining_hp = enemy_boxes - current_enemy_boxes

    enemy_hp_display = red_box * current_enemy_boxes
    enemy_remaining_hp_display = ' ' * enemy_remaining_hp

    print("--------------------------------------------------------------------\n")
    print(enemy.name + " HP: " + str(current_enemy_hp) + "\n")
    print(str(enemy_hp_display) + str(enemy_remaining_hp_display) + "\n")
    print("\n")
    print((player.name) + " HP: " + str(player.hp) + "\n")
    print(str(player_hp_display) + str(player_remaining_hp_display) + "\n")
    print("--------------------------------------------------------------------\n")


"""
The function to calculate the player's weapon damage

WIP
"""


def player_attack_weapon(player, enemy, current_enemy_hp):
    player_damage = player.strength + player.main_hand.prop

    print(player.name + " attacks!\n")
    print(player.name + " deals " + str(player_damage) +
          " damage to " + enemy.name + "!\n")

    current_enemy_hp -= player_damage
    if (current_enemy_hp < 0):
        current_enemy_hp = 0

    return current_enemy_hp


"""
The function to calculate the player's magic damage

WIP
"""


def player_attack_magic(player, enemy, current_enemy_hp):
    player_damage = player.intelligence

    print(player.name + " cast magic!\n")
    print(player.name + " deals " + str(player_damage) +
          " damage to " + enemy.name + "!\n")

    current_enemy_hp -= player_damage
    if (current_enemy_hp < 0):
        current_enemy_hp = 0

    return current_enemy_hp


"""
The function to calculate the player's item usage

WIP
"""


def player_use_item(player):
    player_heal = 30

    print(player.name + " uses a potion!\n")

    if (player.hp + player_heal > player.vigor*10):
        player_heal = player.vigor*10 - player.hp

    print(player.name + " heals " + str(player_heal) + " HP!\n")

    player.hp += player_heal

    return


"""
The function to calculate the result of the player trying to flee
WIP
"""


def player_flee(player):
    while True:
        player_choice = input(
            "Are you sure you want to flee?\n1. Yes    2. No\n\n").lower()

        if player_choice not in player_flee_input_map:
            print("Invalid choice, please choose again.\n")
            continue
        else:
            player_choice = player_flee_input_map[player_choice]
            return player_choice


def enemy_action(player, enemy):

    print("The " + enemy.name + " takes it's turn.\n")
    time.sleep(1)

    enemy_attack_weapon(player, enemy)
    return


def enemy_attack_weapon(player, enemy):
    enemy_damage = enemy.strength - player.armour.prop

    print(enemy.name + " attacks!\n")
    print(enemy.name + " deals " + str(enemy_damage) +
          " damage to " + player.name + "!\n")

    player.hp -= enemy_damage

    return


"""
Things left to add:
    Enemy attacks
    Enemy spells
    Enemy AI
"""
