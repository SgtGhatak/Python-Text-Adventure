import os
import time
import random
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
    combat_result = combat(player, enemy, enemy.hp)

    return combat_result


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


def combat(player, enemy, enemy_max_hp):
    while (player.hp > 0 and enemy.hp > 0):
        cls()
        combat_ui(player, enemy, enemy_max_hp)

        player_input = player_choices(player)

        if (player_input == 'Attack'):
            player_attack_weapon(player, enemy)
        elif (player_input == 'Magic'):
            player_choose_spell(player, enemy)
        elif (player_input == 'Item'):
            player_use_item(player)
        elif (player_input == 'Flee'):
            player_flee_choice = player_flee(player)
            if (player_flee_choice == 'Yes'):
                print(player.name + " has successfully fled!\n")
                return 0
            else:
                continue

        if (enemy.hp <= 0):
            continue

        time.sleep(1)
        enemy_action(player, enemy)
        pause()

    if (player.checkIfDead() == 1):
        print("The player has died...\n")
        return -1
    else:
        print("The enemy is dead!\n")
        return 1


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


def combat_ui(player, enemy, enemy_max_hp):
    # player's calculations
    max_player_hp = player.vigor
    player_hp_box = (player.vigor)/10

    player_boxes = int(max_player_hp/player_hp_box)
    current_player_boxes = int(player.hp/player_hp_box)
    if (player.hp % player_hp_box > 0 and current_player_boxes < 10):
        current_player_boxes += 1
    player_remaining_hp = player_boxes - current_player_boxes

    player_hp_display = green_box * current_player_boxes
    player_remaining_hp_display = ' ' * player_remaining_hp

    # enemy's calculations
    max_enemy_hp = enemy_max_hp
    enemy_hp_box = (enemy_max_hp)/10

    enemy_boxes = int(max_enemy_hp/enemy_hp_box)
    current_enemy_boxes = int(enemy.hp/enemy_hp_box)
    if (enemy.hp % enemy_hp_box > 0 and current_enemy_boxes < 10):
        current_enemy_boxes += 1
    enemy_remaining_hp = enemy_boxes - current_enemy_boxes

    enemy_hp_display = red_box * current_enemy_boxes
    enemy_remaining_hp_display = ' ' * enemy_remaining_hp

    print("--------------------------------------------------------------------\n")
    print(enemy.name + " HP: " + str(enemy.hp) + "\n")
    print(str(enemy_hp_display) + str(enemy_remaining_hp_display) + "\n")
    print("\n")
    print((player.name) + " HP: " + str(player.hp) + "\n")
    print(str(player_hp_display) + str(player_remaining_hp_display) + "\n")
    print("--------------------------------------------------------------------\n")


"""
The function to calculate the player's weapon damage

WIP
"""


def player_attack_weapon(player, enemy):

    modifier = int(player.strength/2 - 5)

    player_attack = calculate_attack(player.proficiency, modifier)
    player_damage = calculate_damage(player.main_hand.prop, modifier)

    print(player.name + " attacks " + enemy.name + "\n")
    time.sleep(1)
    if (player_attack < enemy.ac):
        print(player.name + " misses their attack.\n")
        return
    else:
        print(player.name + " hits!\n")
    time.sleep(1)
    print(player.name + " deals " + str(player_damage) +
          " damage to " + enemy.name + "!\n")

    enemy.hp -= player_damage
    if (enemy.hp < 0):
        enemy.hp = 0

    return


"""
The function to calculate the player's magic damage

WIP
"""


def player_choose_spell(player, enemy):

    spell_map = {str(i.id): i.name for i in player.spells}

    if (len(player.spells) == 0):
        print("You have no spells\n")
        return

    while True:
        print("Choose your spell.\n")
        for i in player.spells:
            print("{}. {}".format(i.id, i.name))
        chosen_spell = input("\n").lower()

        if chosen_spell not in spell_map:
            print("Invalid choice, please choose again.\n")
            continue
        else:
            chosen_spell = spell_map[chosen_spell]
            break

    for i in player.spells:
        if (chosen_spell == i.name):
            chosen_spell = i

    if (chosen_spell.category == "Miracle"):
        modifier = int(player.faith/2 - 5)

        if (chosen_spell.type == "Heal"):
            player_heal_magic(player, chosen_spell, modifier)

    if (chosen_spell.category == "Spell"):
        modifier = int(player.intelligence/2 - 5)

        if(chosen_spell.type == "Attack"):
            player_attack_magic(player, enemy, chosen_spell, modifier)


def player_heal_magic(player, spell, modifier):
    dice = spell.prop.split("d")

    heal = modifier
    for i in range(int(dice[0])):
        heal += random.randint(1, int(dice[1]))

    print(player.name + " cast " + spell.name + ".\n")
    print(player.name + " heals " + str(heal) + "!\n")

    player.hp += heal

    if (player.hp > player.vigor):
        player.hp = player.vigor


def player_attack_magic(player, enemy, spell, modifier):
    player_attack = calculate_attack(player.proficiency, modifier)
    player_damage = calculate_damage(spell.prop, modifier)

    print(player.name + " casts " + spell.name + "!\n")
    time.sleep(1)
    if (player_attack < enemy.ac):
        print(player.name + " misses their attack.\n")
        return
    else:
        print(player.name + " hits!\n")
    time.sleep(1)
    print(player.name + " deals " + str(player_damage) +
          " damage to " + enemy.name + "!\n")

    enemy.hp -= player_damage
    if (enemy.hp < 0):
        enemy.hp = 0

    return


"""
The function to calculate the player's item usage

WIP
"""


def player_use_item(player):
    player_heal = random.randint(1, 8)

    print(player.name + " uses a potion!\n")

    if (player.hp + player_heal > player.vigor*10):
        player_heal = player.vigor - player.hp

    print(player.name + " heals " + str(player_heal) + " HP!\n")

    player.hp += player_heal

    if (player.hp > player.vigor):
        player.hp = player.vigor

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
    if (enemy.strength >= enemy.dexterity):
        modifier = int(enemy.strength/2 - 5)
    else:
        modifier = int(enemy.dexterity/2 - 5)

    enemy_attack = calculate_attack(enemy.proficiency, modifier)
    enemy_damage = calculate_damage(enemy.damage, modifier)

    print(enemy.name + " attacks " + player.name + "\n")
    time.sleep(1)
    if (enemy_attack < player.ac):
        print(enemy.name + " misses their attack.\n")
        return
    else:
        print(enemy.name + " hits!\n")
    time.sleep(1)
    print(enemy.name + " deals " + str(enemy_damage) +
          " damage to " + player.name + "!\n")

    player.hp -= enemy_damage

    return


def calculate_attack(proficiency, modifier):
    modifier = modifier + proficiency

    attack = random.randint(1, 20) + modifier

    return attack


def calculate_damage(damage_dice, modifier):
    dice = damage_dice.split("d")
    damage = 0

    for i in range(int(dice[0])):
        damage += random.randint(1, int(dice[1]))

    damage = damage + modifier

    if damage < 0:
        damage = 0

    return damage


"""
Things left to add:
    Enemy attacks
    Enemy spells
    Enemy AI
"""
