import random

class Item:
    def __init__(self, name, type, description, prop):
        self.name = name
        self.type = type
        self.description = description
        self.prop = prop

    def generate_item_dmg(self):
        dmgl = self.prop - 15
        dmgh = self.prop + 15
        return random.randrange(dmgl, dmgh)

