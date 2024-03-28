from pokemon import Pokemon
from random import randint
from type import *

Dracaufeu = Pokemon("Dracaufeu", 300, Type.SPECTRE, 250, "Growl", 5, Type.NORMAL, "Ember", 20, Type.FEU)
Tortank = Pokemon("Tortank", 350, Type.EAU, 100, "Head butt", 10, Type.NORMAL, "Water Canon", 25, Type.EAU)
print("--------------------", Tortank.type.value,"--------------------")

nbTours = 0
while Dracaufeu.is_alive() and Tortank.is_alive():
    nbTours += 1
    print('---------------------------')
    print("Début du tours  :  ", nbTours)
    print('---------------------------')
    if randint(1,2) == 1:
        numAtk = int(input(f"Numéro de l'attaque choisie pour Dracaufeu :  (1) {Dracaufeu.atkNom[0]}  (2) {Tortank.atkNom[1]} ")) - 1
        while numAtk != 0 and numAtk != 1:
            numAtk = int(input(f"Numéro de l'attaque choisie pour Dracaufeu :  (1) {Dracaufeu.atkNom[0]}  (2) {Tortank.atkNom[1]} ")) - 1
        Tortank.DamageTaken(Dracaufeu.atkDmg[numAtk], Dracaufeu.atkType[numAtk].value)
        print("Dracaufeu attaque Tortank de ",Dracaufeu.atkDmg[numAtk] , "      Tortank a encore  : ", Tortank.hp)
        if not (Tortank.is_alive()):
            print("Tortank fainted")
            print('---------------------------')
            break
        numAtk = int(input(f"Numéro de l'attaque choisie pour Tortank :  (1) {Tortank.atkNom[0]}  (2) {Dracaufeu.atkNom[1]} ")) - 1
        while numAtk != 0 and numAtk != 1:
            numAtk = int(input(f"Numéro de l'attaque choisie pour Dracaufeu :  (1) {Dracaufeu.atkNom[0]}  (2) {Tortank.atkNom[1]} ")) - 1
        Dracaufeu.DamageTaken(Tortank.atkDmg[numAtk], Tortank.atkType[numAtk].value)
        print("Tortank attaque Dracaufeu de ",Tortank.atkDmg[numAtk] , "      Dracaufeu a encore  : ", Dracaufeu.hp)
        if not (Dracaufeu.is_alive()):
            print("Dracaufeu fainted")
            print('---------------------------')
            break
    else:
        numAtk = int(input(f"Numéro de l'attaque choisie pour Tortank :  (1) {Tortank.atkNom[0]}  (2) {Dracaufeu.atkNom[1]} ")) - 1
        Dracaufeu.DamageTaken(Tortank.atkDmg[numAtk], Tortank.atkType[numAtk].value)
        while numAtk != 0 and numAtk != 1:
            numAtk = int(input(f"Numéro de l'attaque choisie pour Dracaufeu :  (1) {Dracaufeu.atkNom[0]}  (2) {Tortank.atkNom[1]} ")) - 1
        print("Tortank attaque Dracaufeu de ",Tortank.atkDmg[numAtk] , "      Dracaufeu a encore  : ", Dracaufeu.hp)
        if not (Dracaufeu.is_alive()):
            print("Dracaufeu fainted")
            print('---------------------------')
            break
        numAtk = int(input(f"Numéro de l'attaque choisie pour Dracaufeu :  (1) {Dracaufeu.atkNom[0]}  (2) {Tortank.atkNom[1]} ")) - 1
        while numAtk != 0 and numAtk != 1:
            numAtk = int(input(f"Numéro de l'attaque choisie pour Dracaufeu :  (1) {Dracaufeu.atkNom[0]}  (2) {Tortank.atkNom[1]} ")) - 1
        Tortank.DamageTaken(Dracaufeu.atkDmg[numAtk], Dracaufeu.atkType[numAtk].value)
        print("Dracaufeu attaque Tortank de ",Dracaufeu.atkDmg[numAtk] , "      Tortank a encore  : ", Tortank.hp)
        if not (Tortank.is_alive()):
            print("Tortank fainted")
            print('---------------------------')
            break

    
if Dracaufeu.is_alive():
    print("Dracaufeu gagne ce combat !!")
else:
    print("Tortank gagne ce combat !!")

    


