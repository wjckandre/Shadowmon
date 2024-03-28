from type import *


class Pokemon:
    def __init__(self, nom, hp, type, speed, atkNom1, atkDmg1, atkType1, atkNom2, atkDmg2, atkType2):
        self.nom = nom
        self.type = type
        self.hp = hp
        self.hpMax = hp
        self.speed = speed
        self.atkNom = [atkNom1, atkNom2]
        self.atkDmg = [atkDmg1, atkDmg2]
        self.atkType = [atkType1, atkType2]
    
    def DamageTaken(self, damage, type):
        if self.hp > damage*TypeChart[type][self.type.value]:
            self.hp -= damage*TypeChart[type][self.type.value]
        else:
            self.hp = 0

    def AddHp(self, heal):
        if self.hpMax < heal+self.hp :
            self.hp = self.hpMax
        else:
            self.hp += heal
    
    def is_alive(self):
        return self.hp != 0
    

    