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
            self.Pokemon.pokemon_fighting.AddHp(20)
            return 20
        if item == Item.super_potion:
            self.super_potions -= 1
            self.Pokemon.pokemon_fighting.AddHp(60)
            return 60
        if item == Item.hyper_potion:
            self.hyper_potions -= 1
            self.Pokemon.pokemon_fighting.AddHp(120)
            return 120
        if item == Item.revive:
            self.revive -= 1
            self.Pokemon.pokemon_fighting.Revive()
            return 1000

def Def_Items(item):
    if item == "potions" or item == "p":
        return Item.potion
    if item == "super potions" or item == "sp":
        return Item.super_potion
    if item == "hyper potions" or item == "hp":
        return Item.hyper_potion
    if item == "revive" or item == "r":
        return Item.revive
    

class Item(Enum):
    potion = 0
    super_potion = 1
    hyper_potion = 2
    revive = 3