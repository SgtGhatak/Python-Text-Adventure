from classes import *


def combat_init(player, enemy):
    current_enemy_hp = enemy.vigor*10

    combat_result = combat(player, enemy, current_enemy_hp)

    return


def combat(player, enemy, current_enemy_hp):
    combat_ui(player, enemy, current_enemy_hp)

    if (player.checkIfDead() == 1):
        print("The player has died...\n")
        return -1
    elif (current_enemy_hp <= 0):
        print("The enemy is dead!\n")
        return 1

    player_input = player_choices(player)

    if (player_input == '1' or player_input.lower() == 'attack'):
        current_enemy_hp = player_attack_weapon(
            player, enemy, current_enemy_hp)
    elif (player_input == '2' or player_input.lower() == 'magic'):
        current_enemy_hp = player_attack_magic(
            player, enemy, current_enemy_hp)
    elif (player_input == '3' or player_input.lower() == 'item'):
        player_use_item(player)
    elif (player_input == '4' or player_input.lower() == 'flee'):
        if (player_flee(player) == 1):
            return 0

    combat(player, enemy, current_enemy_hp)


def player_choices(player):
    print("What would " + player.name + " like to do?\n")
    print("1. Attack     3. Item\n")
    print("2. Magic      4. Flee\n")
    player_input = str(input().lower())
    print("\n")

    print(player_input)

    if (player_input != '1' and player_input != 'attack' and player_input != '2' and player_input != 'magic' and player_input != '3' and player_input != 'item' and player_input != '4' and player_input != 'flee'):
        print("Invalid choice, please choose again.\n")
        player_choices(player)
    return player_input


def combat_ui(player, enemy, current_enemy_hp):
    max_player_hp = player.vigor*10
    player_hp_box = (player.vigor*10)/10

    player_boxes = int(max_player_hp/player_hp_box)
    current_player_boxes = int(player.hp/player_hp_box)
    player_remaining_hp = player_boxes - current_player_boxes

    player_hp_display = '\U0001F7E9' * current_player_boxes
    player_remaining_hp_display = ' ' * player_remaining_hp

    max_enemy_hp = enemy.vigor*10
    enemy_hp_box = (enemy.vigor*10)/10

    enemy_boxes = int(max_enemy_hp/enemy_hp_box)
    current_enemy_boxes = int(current_enemy_hp/enemy_hp_box)
    enemy_remaining_hp = enemy_boxes - current_enemy_boxes

    enemy_hp_display = '\U0001F7E5' * current_enemy_boxes
    enemy_remaining_hp_display = ' ' * enemy_remaining_hp

    print("--------------------------------------------------------------------\n")
    print(enemy.name + " HP: " + str(current_enemy_hp) + "\n")
    print(str(enemy_hp_display) + str(enemy_remaining_hp_display) + "\n")
    print("\n")
    print((player.name) + " HP: " + str(player.hp) + "\n")
    print(str(player_hp_display) + str(player_remaining_hp_display) + "\n")
    print("--------------------------------------------------------------------\n")

    if (player.checkIfDead() == 1):
        return 2
    elif (current_enemy_hp <= 0):
        return 1
    else:
        return 0


def player_attack_weapon(player, enemy, current_enemy_hp):
    player_damage = player.strength

    print(player.name + " attacks!\n")
    print(player.name + " deals " + str(player_damage) +
          " damage to " + enemy.name + "!\n")

    current_enemy_hp -= player_damage

    return current_enemy_hp


def player_attack_magic(player, enemy, current_enemy_hp):
    player_damage = player.intelligence

    print(player.name + " cast magic!\n")
    print(player.name + " deals " + str(player_damage) +
          " damage to " + enemy.name + "!\n")

    current_enemy_hp -= player_damage

    return current_enemy_hp


def player_use_item(player):
    player_heal = 30

    print(player.name + " uses a potion!\n")

    if (player.hp + player_heal > player.vigor*10):
        player_heal = player.vigor*10 - player.hp

    print(player.name + " heals " + str(player_heal) + " HP!\n")

    player.hp += player_heal

    return


def player_flee(player):

    confirm = input("Are you sure you want to flee?\n1. Yes    2. No").lower()

    if (confirm == '1' or confirm == 'yes'):
        print(player.name + " flees!\n")
        return 1
    elif (confirm == '2' or confirm == 'no'):
        return 0

    print("Invalid choice, please choose again.\n")
    player_flee(player)
