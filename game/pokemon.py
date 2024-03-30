from type import *


class Pokemon:
    def __init__(self, nom, hp, type, speed, nbAtk, atkNom, atkDmg, atkType):
        self.nom = nom
        self.type = type
        self.hp = hp
        self.hpMax = hp
        self.speed = speed
        self.nbAtk = nbAtk
        self.atkNom = atkNom
        self.atkDmg = atkDmg
        self.atkType = atkType
    
    def DamageTaken(self, damage):
        if self.hp > damage:
            self.hp -= damage
        else:
            self.hp = 0

    def AddHp(self, heal):
        if self.hpMax < heal+self.hp :
            self.hp = self.hpMax
        else:
            self.hp += heal
    
    def is_alive(self):
        return self.hp != 0
    

    