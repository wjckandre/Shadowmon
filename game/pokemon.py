
class Pokemon:
    def __init__(self, nom, hp, type, speed, atkDmg1, atkDmg2, atkType1, atkType2):
        self.nom = nom
        self.type = type
        self.hp = hp
        self.hpMax = hp
        self.speed = speed
        self.atkDmg1 = atkDmg1
        self.atkDmg2 = atkDmg2
        self.atkType1 = atkType1
        self.atkType2 = atkType2
    
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
    

    