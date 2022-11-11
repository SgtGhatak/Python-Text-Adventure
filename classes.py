class Player:
    def __init__(self, id, name, vigor, focus, strength, dexterity, intelligence, faith):
        self.id = id
        self.name = name
        self.vigor = vigor
        self.focus = focus
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.faith = faith
        self.hp = vigor * 10
        self.mp = focus * 10

        self.inventory = []
        self.spells = []

        self.main_hand = None
        self.off_hand = None
        self.armour = None

    def checkIfDead(self):
        if(self.hp <= 0):
            return 1
        else:
            return 0

    def healToFull(self):
        self.hp = self.vigor * 10
        self.mp = self.focus * 10


class Item():
    def __init__(self, name, prop, type, category):
        self.name = name
        self.prop = prop
        self.type = type
        self.category = category


class Enemy:
    def __init__(self, id, name, vigor, focus, strength, dexterity, intelligence, faith, difficulty):
        self.id = id
        self.name = name
        self.vigor = vigor
        self.focus = focus
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.faith = faith
        self.difficulty = difficulty
