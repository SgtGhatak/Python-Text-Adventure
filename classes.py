class Player:
    def __init__(self, id, name, vigor, focus, strength, dexterity, intelligence, faith, hp, mp):
        self.id = id
        self.name = name
        self.vigor = vigor
        self.focus = focus
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.faith = faith
        self.hp = hp
        self.mp = mp


class Enemy:
    def __init__(self, id, name, vigor, focus, strength, dexterity, intelligence, faith, difficulty):
        self.id = id
        self.name = name
        self.vig = vigor
        self.foc = focus
        self.str = strength
        self.dex = dexterity
        self.int = intelligence
        self.fth = faith
        self.diff = difficulty
