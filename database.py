import sqlite3


def InitDB():
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
    player_spells(player_spell_id INTEGER
    name TEXT,
    prop INTEGER,
    type TEXT,
    category TEXT,
    PRIMARY KEY (player_spell_id))
    """

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
