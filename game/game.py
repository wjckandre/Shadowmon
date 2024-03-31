from pokemon import Pokemon
from random import randint
from type import *
from recognition.API import SearchCard, CameraPhotoTexte, SearchPokemon


# Pokemon1 = Pokemon("Dracaufeu", 300, Type.FEU, 250, "Growl", 5, Type.NORMAL, "Ember", 20, Type.FEU)
# Pokemon2 = Pokemon("Tortank", 350, Type.EAU, 100, "Head butt", 10, Type.NORMAL, "Water Canon", 25, Type.EAU)

#########################   POKEMON 1   #########################
txt = CameraPhotoTexte()
carte = SearchCard(txt)
print(carte)
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


nbTours = 0
while Pokemon1.is_alive() and Pokemon2.is_alive():
    nbTours += 1
    print('---------------------------')
    print("Début du tours  :  ", nbTours)
    print('---------------------------')
    ########################################################   CHOIX DES ATTAQUES   ########################################################
    numAtkPoke1 = int(input(f"Numéro de l'attaque choisie pour {Pokemon1.nom} :  (1) {Pokemon1.atkNom[0]} / {Pokemon1.atkDmg[0]}  (2) {Pokemon1.atkNom[1]} / {Pokemon1.atkDmg[1]}   :")) - 1
    numAtkPoke2 = int(input(f"Numéro de l'attaque choisie pour {Pokemon2.nom} :  (1) {Pokemon2.atkNom[0]} / {Pokemon2.atkDmg[0]}  (2) {Pokemon2.atkNom[1]} / {Pokemon2.atkDmg[1]}   :")) - 1
    while numAtkPoke1 != 0 and numAtkPoke1 != 1:
        numAtkPoke1 = int(input(f"Numéro de l'attaque choisie pour {Pokemon1.nom} :  (1) {Pokemon1.atkNom[0]} / {Pokemon1.atkDmg[0]}  (2) {Pokemon1.atkNom[1]} / {Pokemon1.atkDmg[1]}   :")) - 1
    while numAtkPoke2 != 0 and numAtkPoke2 != 1:
        numAtkPoke2 = int(input(f"Numéro de l'attaque choisie pour {Pokemon2.nom} :  (1) {Pokemon2.atkNom[0]} / {Pokemon2.atkDmg[0]}  (2) {Pokemon2.atkNom[1]} / {Pokemon2.atkDmg[1]}   :")) - 1   

    if randint(1,2) == 1: # CHOI DU JOUEUR PRIORITAIRE
        ########################################################   ATTAQUE DES POKEMONS   ######################################################## '
        Pokemon2.DamageTaken(Pokemon1.atkDmg[numAtkPoke1]*Avantage_type(Pokemon1.type, Pokemon2.type))
        print(f"{Pokemon1.nom} attaque {Pokemon2.nom} de ",Pokemon1.atkDmg[numAtkPoke1]*Avantage_type(Pokemon1.type, Pokemon2.type) , f"      {Pokemon2.nom} a encore  : ", Pokemon2.hp)
        if not (Pokemon2.is_alive()):
            print(f"{Pokemon2.nom} fainted")
            print('---------------------------')
            break
        Pokemon1.DamageTaken(Pokemon2.atkDmg[numAtkPoke2]*Avantage_type(Pokemon2.type, Pokemon1.type))
        print(f"{Pokemon2.nom} attaque {Pokemon1.nom} de ",Pokemon2.atkDmg[numAtkPoke2]*Avantage_type(Pokemon2.type, Pokemon1.type) , f"      {Pokemon1.nom} a encore  : ", Pokemon1.hp)
        if not (Pokemon1.is_alive()):
            print(f"{Pokemon1.nom} fainted")
            print('---------------------------')
            break
    else:
        ########################################################   ATTAQUE DES POKEMONS   ########################################################
        Pokemon1.DamageTaken(Pokemon2.atkDmg[numAtkPoke2]*Avantage_type(Pokemon2.type, Pokemon1.type))
        print(f"{Pokemon2.nom} attaque {Pokemon1.nom} de ",Pokemon2.atkDmg[numAtkPoke2]*Avantage_type(Pokemon2.type, Pokemon1.type) , f"      {Pokemon1.nom} a encore  : ", Pokemon1.hp)
        if not (Pokemon1.is_alive()):
            print(f"{Pokemon1.nom} fainted")
            print('---------------------------')
            break
        Pokemon2.DamageTaken(Pokemon1.atkDmg[numAtkPoke1]*Avantage_type(Pokemon1.type, Pokemon2.type))
        print(f"{Pokemon1.nom} attaque {Pokemon2.nom} de ",Pokemon1.atkDmg[numAtkPoke1]*Avantage_type(Pokemon1.type, Pokemon2.type) , f"      {Pokemon2.nom} a encore  : ", Pokemon2.hp)
        if not (Pokemon2.is_alive()):
            print(f"{Pokemon2.nom} fainted")
            print('---------------------------')
            break

    
if Pokemon1.is_alive():
    print(f"{Pokemon1.nom} gagne ce combat !!")
else:
    print(f"{Pokemon2.nom} gagne ce combat !!")

    


