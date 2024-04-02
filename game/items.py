from enum import Enum


class Items():
    def __init__(self, Pokemon, potions, super_potions, hyper_potions, revive):
        self.potions = potions
        self.super_potions = super_potions
        self.hyper_potions = hyper_potions
        self.revive = revive
        self.Pokemon = Pokemon

    def Use(self, item):
        if item == Item.potion:
            self.potions -= 1
            self.Pokemon.AddHp(20)
            return 20
        if item == Item.super_potion:
            self.super_potions -= 1
            self.Pokemon.AddHp(60)
            return 60
        if item == Item.hyper_potion:
            self.hyper_potions -= 1
            self.Pokemon.AddHp(120)
            return 120
        if item == Item.revive:
            self.revive -= 1
            self.Pokemon.AddHp(1000)
            return 1000

def Def_Items(item):
    if item == "potions":
        return Item.potion
    if item == "super potions":
        return Item.super_potion
    if item == "hyper potions":
        return Item.hyper_potion
    if item == "revive":
        return Item.revive
    

class Item(Enum):
    potion = 1
    super_potion = 2
    hyper_potion = 3
    revive = 4