from pokemon import Pokemon
from random import randint

Dracaufeu = Pokemon("Dracaufeu", 300, "Feu" , 150, 25, 10, "Feu", "Normal")
Tortank = Pokemon("Tortank", 350, "Eau", 100, 20, 10, "Eau", "Normal")

nbTours = 0
while Dracaufeu.is_alive() and Tortank.is_alive():
    nbTours += 1
    print('---------------------------')
    print("Début du tours  :  ", nbTours)
    print('---------------------------')
    if Dracaufeu.speed > Tortank.speed:
        if randint(1,2) == 1:
            Tortank.DamageTaken(Dracaufeu.atkDmg1)
            print("Dracaufeu attaque Tortank de ",Dracaufeu.atkDmg1 , "      Tortank a encore  : ", Tortank.hp)
        else:
            Tortank.DamageTaken(Dracaufeu.atkDmg2)
            print("Dracaufeu attaque Tortank de ",Dracaufeu.atkDmg2 , "      Tortank a encore  : ", Tortank.hp)
        if not (Tortank.is_alive()):
            print("Tortank fainted")
            print('---------------------------')
            break
        if randint(1,2) == 1:
            Dracaufeu.DamageTaken(Tortank.atkDmg1)
            print("Tortank attaque Dracaufeu de ",Tortank.atkDmg1 , "      Dracaufeu a encore  : ", Dracaufeu.hp)
        else:
            Dracaufeu.DamageTaken(Tortank.atkDmg2)
            print("Tortank attaque Dracaufeu de ",Tortank.atkDmg2 , "      Dracaufeu a encore  : ", Dracaufeu.hp)
        if not (Dracaufeu.is_alive()):
            print("Dracaufeu fainted")
            print('---------------------------')
            break
    elif Dracaufeu.speed < Tortank.speed:
        if randint(1,2) == 1:
            print("Tortank attaque Dracaufeu de ",Tortank.atkDmg1 , "      Dracaufeu a encore  : ", Dracaufeu.hp)
            Dracaufeu.DamageTaken(Tortank.atkDmg1)
        else:
            Dracaufeu.DamageTaken(Tortank.atkDmg2)
            print("Tortank attaque Dracaufeu de ",Tortank.atkDmg2 , "      Dracaufeu a encore  : ", Dracaufeu.hp)
        if not (Dracaufeu.is_alive()):
            print("Dracaufeu fainted")
            print('---------------------------')
            break
        if randint(1,2) == 1:
            Tortank.DamageTaken(Dracaufeu.atkDmg1)
            print("Dracaufeu attaque Tortank de ",Dracaufeu.atkDmg1 , "      Tortank a encore  : ", Tortank.hp)
        else:
            Tortank.DamageTaken(Dracaufeu.atkDmg2)
            print("Dracaufeu attaque Tortank de ",Dracaufeu.atkDmg2 , "      Tortank a encore  : ", Tortank.hp)
        if not (Tortank.is_alive()):
            print("Tortank fainted")
            print('---------------------------')
            break


    
if Dracaufeu.is_alive():
    print("Dracaufeu gagne ce combat !!")
else:
    print("Tortank gagne ce combat !!")

    


