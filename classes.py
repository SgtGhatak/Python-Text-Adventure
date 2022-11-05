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

    def checkIfDead(self):
        if(self.hp <= 0):
            return 1
        else:
            return 0

    def healToFull(self):
        self.hp = self.vigor * 100
        self.mp = self.focus * 100


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
