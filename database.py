import sqlite3


def init_DB():
    # define connection and cursor
    connnect = sqlite3.connect('gameDatabase.db')
    cursor = connnect.cursor()

    # create player tale

    create_player_table = """CREATE TABLE IF NOT EXISTS
    players(player_id INTEGER,
    name TEXT,
    vigor INTEGER,
    focus INTEGER,
    strength INTEGER,
    dexterity INTEGER,
    intelligence INTEGER,
    faith INTEGER,
    hp INTEGER,
    mp INTEGER,
    PRIMARY KEY (player_id))
    """

    cursor.execute(create_player_table)

    # crete player_times table

    create_player_items_table = """CREATE TABLE IF NOT EXISTS
    player_items(player_item_id INTEGER,
    name TEXT,
    prop TEXT,
    type TEXT,
    category TEXT,
    PRIMARY KEY (player_item_id))
    """

    cursor.execute(create_player_items_table)

    # create player_data table

    create_player_data_table = """CREATE TABLE IF NOT EXISTS
    player_data(player_id INTEGER,
    player_item_id INTEGER,
    quantity INTEGER,
    PRIMARY KEY (player_id, player_item_id),
    FOREIGN KEY(player_id) REFERENCES players(player_id),
    FOREIGN KEY(player_item_id) REFERENCES player_items(player_item_id))
    """

    cursor.execute(create_player_data_table)

    # create player_spells table

    create_player_spells_table = """CREATE TABLE IF NOT EXISTS
    player_spells(player_spell_id INTEGER,
    name TEXT,
    prop INTEGER,
    type TEXT,
    category TEXT,
    PRIMARY KEY (player_spell_id))
    """

    cursor.execute(create_player_spells_table)

    # create items table

    create_items_table = """CREATE TABLE IF NOT EXISTS
    items(item_id INTEGER,
    name TEXT,
    prop TEXT,
    type TEXT,
    category TEXT,
    PRIMARY KEY (item_id))
    """

    cursor.execute(create_items_table)

    # create spells table

    create_spells_table = """CREATE TABLE IF NOT EXISTS
    spells(spell_id INTEGER,
    name TEXT,
    prop INTEGER,
    type TEXT,
    category TEXT,
    PRIMARY KEY (spell_id))
    """

    cursor.execute(create_spells_table)

    connnect.commit()
    cursor.close()

    # # get rows
    # cursor.execute("SELECT COUNT(*) FROM players")
    # results = cursor.fetchone()
    # print(results[0])

    # # insert values into players table

    # cursor.execute(
    #     "INSERT INTO players VALUES (0, 'Harken', 10, 10, 10, 10, 10, 10, 100, 100)")
    # cursor.execute(
    #     "INSERT INTO players VALUES (1, 'Siegfried', 11, 11, 11, 11, 11, 11, 110, 110)")

    # # print results
    # cursor.execute("SELECT * FROM players")

    # results = cursor.fetchall()
    # print(results)

    # # get rows
    # cursor.execute("SELECT COUNT(*) FROM players")
    # results = cursor.fetchone()
    # print(results[0])

    return

# fill in items table


def insert_items_into_db():
    connnect = sqlite3.connect('gameDatabase.db')
    cursor = connnect.cursor()

    cursor.execute("SELECT COUNT(*) FROM items")
    result = cursor.fetchone()

    if (result[0] != 0):
        return

    cursor.execute(
        """
        INSERT INTO items VALUES 
        (1, 'Mace', '1d6', 'Mace', 'Weapon'),
        (2, 'Longsword', '1d8', 'Sword', 'Weapon'),
        (3, 'Greatsword', '2d6', 'Two-handed', 'Weapon'),
        (4, 'Chainmail', '16', 'Medium Armour', 'Armour')
        """)

    connnect.commit()
    cursor.close()


def insert_spells_into_db():
    connnect = sqlite3.connect('gameDatabase.db')
    cursor = connnect.cursor()

    cursor.execute("SELECT COUNT(*) FROM spells")
    result = cursor.fetchone()

    if (result[0] != 0):
        return

    cursor.execute(
        """
        INSERT INTO spells VALUES 
        (1, 'Fire Bolt', '1d10', 'Attack', 'Spell'),
        (2, 'Ice Bolt', '1d8', 'Attack', 'Spell'),
        (3, 'Cure Wounds', '1d8', 'Heal', 'Miracle'),
        (4, 'Holy Smite', '1d8', 'Enchantment', 'Miracle')
        """)

    connnect.commit()
    cursor.close()
