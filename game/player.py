from pokemon import *
from type import *

class Player():
    def __init__(self, name, card1, type1, card2, type2, card3, type3):
        self.name = name

        attacksName = []
        attacksDmg = []
        for x in range (0, len(card1.attacks)):
            attacksName.append(card1.attacks[x].name)
            attacksDmg.append(int(card1.attacks[x].damage))
        attacksName.append(card1.attacks[len(card1.attacks)-1].name)
        attacksDmg.append(int(card1.attacks[len(card1.attacks)-1].damage))
        self.Pokemon1 = Pokemon(card1.name, int(card1.hp), Def_types(type1.types[0]), 0, len(card1.attacks)-1, attacksName, attacksDmg, Def_types(type1.types[0]))

        attacksName = []
        attacksDmg = []
        for x in range (0, len(card2.attacks)):
            attacksName.append(card2.attacks[x].name)
            attacksDmg.append(int(card2.attacks[x].damage))
        attacksName.append(card2.attacks[len(card2.attacks)-1].name)
        attacksDmg.append(int(card2.attacks[len(card2.attacks)-1].damage))
        self.Pokemon2 = Pokemon(card2.name, int(card2.hp), Def_types(type2.types[0]), 0, len(card2.attacks)-1, attacksName, attacksDmg, Def_types(type2.types[0]))

        attacksName = []
        attacksDmg = []
        for x in range (0, len(card3.attacks)):
            attacksName.append(card3.attacks[x].name)
            attacksDmg.append(int(card3.attacks[x].damage))
        attacksName.append(card3.attacks[len(card3.attacks)-1].name)
        attacksDmg.append(int(card3.attacks[len(card3.attacks)-1].damage))
        self.Pokemon3 = Pokemon(card3.name, int(card3.hp), Def_types(type3.types[0]), 0, len(card3.attacks)-1, attacksName, attacksDmg, Def_types(type3.types[0]))

        self.pokemon_fighting = self.Pokemon1

    def Pokemon_fighting(self):
        return self.pokemon_fighting
    
    def Switch_Pokemon(self, pokemon):
        if pokemon == self.Pokemon1.name:
            self.pokemon_fighting = self.Pokemon1
        elif pokemon == self.Pokemon2.name:
            self.pokemon_fighting = self.Pokemon2
        else:
            self.pokemon_fighting = self.Pokemon3
    
    def Is_Team_Dead(self):
        return not(self.Pokemon1.is_alive()) and not(self.Pokemon2.is_alive()) and not(self.Pokemon3.is_alive())
