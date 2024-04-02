from pokemon import Pokemon
from random import randint
from type import *
from recognition.API import SearchCard, CameraPhotoTexte, SearchPokemon
from items import Item, Items, Def_Items

# Pokemon1 = Pokemon("Dracaufeu", 300, Type.FEU, 250, "Growl", 5, Type.NORMAL, "Ember", 20, Type.FEU)
# Pokemon2 = Pokemon("Tortank", 350, Type.EAU, 100, "Head butt", 10, Type.NORMAL, "Water Canon", 25, Type.EAU)

#########################   POKEMON 1   #########################
txt = CameraPhotoTexte()
carte = SearchCard(txt)
pokemon = SearchPokemon(txt)
attacksName = []
attacksDmg = []
for x in range (0, len(carte.attacks)):
    attacksName.append(carte.attacks[x].name)
    attacksDmg.append(int(carte.attacks[x].damage))
attacksName.append(carte.attacks[len(carte.attacks)-1].name)
attacksDmg.append(int(carte.attacks[len(carte.attacks)-1].damage))
Pokemon1 = Pokemon(carte.name, int(carte.hp), Def_types(pokemon.types[0]), 0, len(carte.attacks)-1, attacksName, attacksDmg, Def_types(pokemon.types[0]))

#########################   POKEMON 2   #########################
txt = CameraPhotoTexte()
carte = SearchCard(txt)
pokemon = SearchPokemon(txt)
attacksName = []
attacksDmg = []
for x in range (0, len(carte.attacks)):
    attacksName.append(carte.attacks[x].name)
    attacksDmg.append(int(carte.attacks[x].damage))
attacksName.append(carte.attacks[len(carte.attacks)-1].name)
attacksDmg.append(int(carte.attacks[len(carte.attacks)-1].damage))
Pokemon2 = Pokemon(carte.name, int(carte.hp), Def_types(pokemon.types[0]), 0, len(carte.attacks)-1, attacksName, attacksDmg, Def_types(pokemon.types[0]))

Item_Pokemon1 = Items(Pokemon1,1,1,1,1)
Item_Pokemon2 = Items(Pokemon2,1,1,1,1)


nbTours = 0
while Pokemon1.is_alive() and Pokemon2.is_alive():
    nbTours += 1
    print('---------------------------')
    print("Début du tours  :  ", nbTours)
    print('---------------------------')
    ########################################################   CHOIX DES ATTAQUES   ########################################################
    print(f" Choisissez l'action de {Pokemon1.nom} : ")
    print("-----------------------------------------")
    print("|                   |                   |")
    print("|     ATTAQUE       |       SOINS       |")
    print("|                   |                   |")
    print("-----------------------------------------")
    choixPokemon1 = input()
    if choixPokemon1 == "attaque":
        numAtkPoke1 = int(input(f"Numéro de l'attaque choisie pour {Pokemon1.nom} :  (1) {Pokemon1.atkNom[0]} / {Pokemon1.atkDmg[0]}  (2) {Pokemon1.atkNom[1]} / {Pokemon1.atkDmg[1]}   :")) - 1
        while numAtkPoke1 != 0 and numAtkPoke1 != 1:
            numAtkPoke1 = int(input(f"Numéro de l'attaque choisie pour {Pokemon1.nom} :  (1) {Pokemon1.atkNom[0]} / {Pokemon1.atkDmg[0]}  (2) {Pokemon1.atkNom[1]} / {Pokemon1.atkDmg[1]}   :")) - 1
    else:
        print(f" Potions : {Item_Pokemon1.potions} |  Super Potions : {Item_Pokemon1.super_potions} |  Hyper Potions : {Item_Pokemon1.hyper_potions} |  Revive : {Item_Pokemon1.revive}")
        Item_Pokemon1.Use(Def_Items(input()))
    
    print(f" Choisissez l'action de {Pokemon2.nom} : ")
    print("-----------------------------------------")
    print("|                   |                   |")
    print("|     ATTAQUE       |       SOINS       |")
    print("|                   |                   |")
    print("-----------------------------------------")
    choixPokemon2 = input()
    if choixPokemon2 == 'attaque':
        numAtkPoke2 = int(input(f"Numéro de l'attaque choisie pour {Pokemon2.nom} :  (1) {Pokemon2.atkNom[0]} / {Pokemon2.atkDmg[0]}  (2) {Pokemon2.atkNom[1]} / {Pokemon2.atkDmg[1]}   :")) - 1
        while numAtkPoke2 != 0 and numAtkPoke2 != 1:
            numAtkPoke2 = int(input(f"Numéro de l'attaque choisie pour {Pokemon2.nom} :  (1) {Pokemon2.atkNom[0]} / {Pokemon2.atkDmg[0]}  (2) {Pokemon2.atkNom[1]} / {Pokemon2.atkDmg[1]}   :")) - 1   
    else:
        print(f" Potions : {Item_Pokemon2.potions} |  Super Potions : {Item_Pokemon2.super_potions} |  Hyper Potions : {Item_Pokemon2.hyper_potions} |  Revive : {Item_Pokemon2.revive}")
        Item_Pokemon2.Use(Def_Items(input()))

    
    

    if randint(1,2) == 1: # CHOI DU JOUEUR PRIORITAIRE
        ########################################################   ATTAQUE DES POKEMONS   ######################################################## '
        if choixPokemon1 == "attaque":
            Pokemon2.DamageTaken(Pokemon1.atkDmg[numAtkPoke1]*Avantage_type(Pokemon1.type, Pokemon2.type))
            print(f"{Pokemon1.nom} attaque {Pokemon2.nom} de ",Pokemon1.atkDmg[numAtkPoke1]*Avantage_type(Pokemon1.type, Pokemon2.type))
            if not (Pokemon2.is_alive()):
                print(f"{Pokemon2.nom} fainted")
                print('---------------------------')
                break
        if choixPokemon2 == "attaque":
            Pokemon1.DamageTaken(Pokemon2.atkDmg[numAtkPoke2]*Avantage_type(Pokemon2.type, Pokemon1.type))
            print(f"{Pokemon2.nom} attaque {Pokemon1.nom} de ",Pokemon2.atkDmg[numAtkPoke2]*Avantage_type(Pokemon2.type, Pokemon1.type))
            if not (Pokemon1.is_alive()):
                print(f"{Pokemon1.nom} fainted")
                print('---------------------------')
                break
    else:
        ########################################################   ATTAQUE DES POKEMONS   ########################################################
        if choixPokemon2 == "attaque":
            Pokemon1.DamageTaken(Pokemon2.atkDmg[numAtkPoke2]*Avantage_type(Pokemon2.type, Pokemon1.type))
            print(f"{Pokemon2.nom} attaque {Pokemon1.nom} de ",Pokemon2.atkDmg[numAtkPoke2]*Avantage_type(Pokemon2.type, Pokemon1.type))
            if not (Pokemon1.is_alive()):
                print(f"{Pokemon1.nom} fainted")
                print('---------------------------')
                break
        if choixPokemon1 == "attaque":
            Pokemon2.DamageTaken(Pokemon1.atkDmg[numAtkPoke1]*Avantage_type(Pokemon1.type, Pokemon2.type))
            print(f"{Pokemon1.nom} attaque {Pokemon2.nom} de ",Pokemon1.atkDmg[numAtkPoke1]*Avantage_type(Pokemon1.type, Pokemon2.type))
            if not (Pokemon2.is_alive()):
                print(f"{Pokemon2.nom} fainted")
                print('---------------------------')
                break
    print(f"   -    {Pokemon2.nom} a encore  : ", Pokemon2.hp)
    print(f"   -    {Pokemon1.nom} a encore  : ", Pokemon1.hp)

    
if Pokemon1.is_alive():
    print(f"{Pokemon1.nom} gagne ce combat !!")
else:
    print(f"{Pokemon2.nom} gagne ce combat !!")

    


