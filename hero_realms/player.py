class Player:

    def __init__(self, name):
        self.name = name
        self.gold = 7
        self.life = 50
        self.dmg = 0

    def __str__(self):
        return self.name

    def add_life(self, amount):
        self.life += amount

    def sub_life(self, amount):
        self.life -= amount

    def add_gold(self, amount):
        self.gold += amount

    def sub_gold(self, amount):
        self.gold -= amount

    def add_dmg(self, amount):
        self.dmg += amount

    def sub_dmg(self, amount):
        self.dmg -= amount
