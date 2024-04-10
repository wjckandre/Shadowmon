from pokemon import *
from type import *

class Player():
    def __init__(self,PlayerName, card1_name, card1_hp, card1_type, card1_nb_attack, card1_attack1_name, card1_attack1_dmg, card1_attack2_name, card1_attack2_dmg, card2_name, card2_hp, card2_type, card2_nb_attack, card2_attack1_name, card2_attack1_dmg, card2_attack2_name, card2_attack2_dmg, card3_name, card3_hp, card3_type, card3_nb_attack, card3_attack1_name, card3_attack1_dmg, card3_attack2_name, card3_attack2_dmg):
        self.name = PlayerName
        
        attacksName = [card1_attack1_name, card1_attack2_name]
        attacksDmg = [card1_attack1_dmg, card1_attack2_dmg]
        self.Pokemon1 = Pokemon(card1_name, int(card1_hp), Def_types(card1_type), 0, card1_nb_attack, attacksName, attacksDmg, Def_types(card1_type))

        attacksName = [card2_attack1_name, card2_attack2_name]
        attacksDmg = [card2_attack1_dmg, card2_attack2_dmg]
        self.Pokemon2 = Pokemon(card2_name, int(card2_hp), Def_types(card2_type), 0, card2_nb_attack, attacksName, attacksDmg, Def_types(card2_type))

        attacksName = [card3_attack1_name, card3_attack2_name]
        attacksDmg = [card3_attack1_dmg, card3_attack2_dmg]
        self.Pokemon3 = Pokemon(card3_name, int(card3_hp), Def_types(card3_type), 0, card3_nb_attack, attacksName, attacksDmg, Def_types(card3_type))

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
        return self.pokemon_fighting
    
    def Is_Team_Dead(self):
        return not(self.Pokemon1.is_alive()) and not(self.Pokemon2.is_alive()) and not(self.Pokemon3.is_alive())
