from pokemon import Pokemon
from random import randint
from type import *
from recognition.API import SearchCard, CameraPhotoTexte, SearchPokemon
from items import Item, Items, Def_Items
from player import Player

# Pokemon1 = Pokemon("Dracaufeu", 300, Type.FEU, 250, "Growl", 5, Type.NORMAL, "Ember", 20, Type.FEU)
# Pokemon2 = Pokemon("Tortank", 350, Type.EAU, 100, "Head butt", 10, Type.NORMAL, "Water Canon", 25, Type.EAU)

#########################   POKEMON 1   #########################
txt1 = CameraPhotoTexte()
carte1 = SearchCard(txt1)
pokemon1 = SearchPokemon(txt1)
txt2 = CameraPhotoTexte()
# txt2 = txt1
carte2 = SearchCard(txt2)
pokemon2 = SearchPokemon(txt2)
txt3 = CameraPhotoTexte()
# txt3 = txt1
carte3 = SearchCard(txt3)
pokemon3 = SearchPokemon(txt3)
Player1 = Player("Bob", carte1, pokemon1, carte2, pokemon2, carte3, pokemon3)

print(Player1.Pokemon1.type)
#########################   POKEMON 2   #########################
txt1 = CameraPhotoTexte()
carte1 = SearchCard(txt1)
pokemon1 = SearchPokemon(txt1)
txt2 = CameraPhotoTexte()
# txt2 = txt1
carte2 = SearchCard(txt2)
pokemon2 = SearchPokemon(txt2)
txt3 = CameraPhotoTexte()
# txt3 = txt1
carte3 = SearchCard(txt3)
pokemon3 = SearchPokemon(txt3)
Player2 = Player("Bobis", carte1, pokemon1, carte2, pokemon2, carte3, pokemon3)


Item_Pokemon1 = Items(Player1,1,1,1,1)
Item_Pokemon2 = Items(Player2,1,1,1,1)



nbTours = 0
while not(Player1.Is_Team_Dead()) and  not(Player2.Is_Team_Dead()):
    nbTours += 1
    print('---------------------------')
    print("Début du tours  :  ", nbTours)
    print('---------------------------')
    ########################################################   CHOIX DES ATTAQUES   ########################################################
    print(f" Choisissez l'action de { Player1.Pokemon_fighting().name} : ")
    print("-----------------------------------------")
    print("|                   |                   |")
    print("|     ATTAQUE       |       SOINS       |")
    print("|                   |                   |")
    print("-----------------------------------------")
    print("|                   |                   |")
    print("|     POKEMON       |        FUIR       |")
    print("|                   |                   |")
    print("-----------------------------------------")
    choixPokemon1 = input()
    if choixPokemon1 == "attaque":
        numAtkPoke1 = int(input(f"Numéro de l'attaque choisie pour { Player1.Pokemon_fighting().name} :  (1) { Player1.Pokemon_fighting().atkNom[0]} / { Player1.Pokemon_fighting().atkDmg[0]}  (2) { Player1.Pokemon_fighting().atkNom[1]} / { Player1.Pokemon_fighting().atkDmg[1]}   : ")) - 1
        while numAtkPoke1 != 0 and numAtkPoke1 != 1:
            numAtkPoke1 = int(input(f"Numéro de l'attaque choisie pour { Player1.Pokemon_fighting().name} :  (1) { Player1.Pokemon_fighting().atkNom[0]} / { Player1.Pokemon_fighting().atkDmg[0]}  (2) { Player1.Pokemon_fighting().atkNom[1]} / { Player1.Pokemon_fighting().atkDmg[1]}   : ")) - 1
    elif choixPokemon1 == "soins":
        print(f" Potions : {Item_Pokemon1.potions} |  Super Potions : {Item_Pokemon1.super_potions} |  Hyper Potions : {Item_Pokemon1.hyper_potions} |  Revive : {Item_Pokemon1.revive}")
        Item_Pokemon1.Use(Def_Items(input()))
    elif choixPokemon1 == "pokemon":
        print(f"{Player1.Pokemon1.name}  |  {Player1.Pokemon2.name}  |  {Player1.Pokemon3.name} ")
        Player1.Switch_Pokemon(input())
        while not(Player1.pokemon_fighting.is_alive()):
            print(f"{Player1.Pokemon1.name}  |  {Player1.Pokemon2.name}  |  {Player1.Pokemon3.name} ")
            Player1.Switch_Pokemon(input())
    else:
        print(f"{Player1.name} flew away !  {Player2.name} won the battle")
        break
    
    print(f" Choisissez l'action de { Player2.Pokemon_fighting().name} : ")
    print("-----------------------------------------")
    print("|                   |                   |")
    print("|     ATTAQUE       |       SOINS       |")
    print("|                   |                   |")
    print("-----------------------------------------")
    print("|                   |                   |")
    print("|     POKEMON       |        FUIR       |")
    print("|                   |                   |")
    print("-----------------------------------------")
    choixPokemon2 = input()
    if choixPokemon2 == 'attaque':
        numAtkPoke2 = int(input(f"Numéro de l'attaque choisie pour { Player2.Pokemon_fighting().name} :  (1) { Player2.Pokemon_fighting().atkNom[0]} / { Player2.Pokemon_fighting().atkDmg[0]}  (2) { Player2.Pokemon_fighting().atkNom[1]} / { Player2.Pokemon_fighting().atkDmg[1]}   : ")) - 1
        while numAtkPoke2 != 0 and numAtkPoke2 != 1:
            numAtkPoke2 = int(input(f"Numéro de l'attaque choisie pour { Player2.Pokemon_fighting().name} :  (1) { Player2.Pokemon_fighting().atkNom[0]} / { Player2.Pokemon_fighting().atkDmg[0]}  (2) { Player2.Pokemon_fighting().atkNom[1]} / { Player2.Pokemon_fighting().atkDmg[1]}   : ")) - 1   
    elif choixPokemon2 == "soins":
        print(f" Potions : {Item_Pokemon2.potions} |  Super Potions : {Item_Pokemon2.super_potions} |  Hyper Potions : {Item_Pokemon2.hyper_potions} |  Revive : {Item_Pokemon2.revive}")
        Item_Pokemon2.Use(Def_Items(input()))
    elif choixPokemon2 == "pokemon":
        print(f"{Player2.Pokemon1.name}  |  {Player2.Pokemon2.name}  |  {Player2.Pokemon3.name} ")
        Player2.Switch_Pokemon(input())
        while not(Player2.pokemon_fighting.is_alive()):
            print(" // This Pokemon is dead pick another one // ")
            print(f"{Player2.Pokemon1.name}  |  {Player2.Pokemon2.name}  |  {Player2.Pokemon3.name} ")
            Player2.Switch_Pokemon(input())
    else:
        print(f"{Player2.name} flew away !  {Player1.name} won the battle")
        break


    
    

    if randint(1,2) == 1: # CHOI DU JOUEUR PRIORITAIRE
        ########################################################   ATTAQUE DES POKEMONS   ######################################################## '
        if choixPokemon1 == "attaque":
            Player2.Pokemon_fighting().DamageTaken( Player1.Pokemon_fighting().atkDmg[numAtkPoke1]*Avantage_type( Player1.Pokemon_fighting().type,  Player1.Pokemon_fighting().type))
            print(f"{ Player1.Pokemon_fighting().name} attaque { Player2.Pokemon_fighting().name} de ", Player1.Pokemon_fighting().atkDmg[numAtkPoke1]*Avantage_type( Player1.Pokemon_fighting().type,  Player2.Pokemon_fighting().type))
            if not (Player2.Pokemon_fighting().is_alive()):
                print(f"{ Player2.Pokemon_fighting().name} fainted")
                print('---------------------------')
                if Player2.Is_Team_Dead():
                    break
                print(f"{Player2.Pokemon1.name}  |  {Player2.Pokemon2.name}  |  {Player2.Pokemon3.name} ")
                Player2.Switch_Pokemon(input())
                while not(Player2.pokemon_fighting.is_alive()):
                    print(" // This Pokemon is dead pick another one // ")
                    print(f"{Player2.Pokemon1.name}  |  {Player2.Pokemon2.name}  |  {Player2.Pokemon3.name} ")
                    Player2.Switch_Pokemon(input())
                
        if choixPokemon2 == "attaque":
            Player1.Pokemon_fighting().DamageTaken( Player2.Pokemon_fighting().atkDmg[numAtkPoke2]*Avantage_type( Player2.Pokemon_fighting().type, Player1.Pokemon_fighting().type))
            print(f"{ Player2.Pokemon_fighting().name} attaque { Player1.Pokemon_fighting().name} de ", Player2.Pokemon_fighting().atkDmg[numAtkPoke2]*Avantage_type( Player2.Pokemon_fighting().type, Player1.Pokemon_fighting().type))
            if not ( Player1.Pokemon_fighting().is_alive()):
                print(f"{ Player1.Pokemon_fighting().name} fainted")
                print('---------------------------')
                if Player1.Is_Team_Dead():
                    break
                print(f"{Player1.Pokemon1.name}  |  {Player1.Pokemon2.name}  |  {Player1.Pokemon3.name} ")
                Player1.Switch_Pokemon(input())
                while not(Player1.pokemon_fighting.is_alive()):
                    print(" // This Pokemon is dead pick another one // ")
                    print(f"{Player1.Pokemon1.name}  |  {Player1.Pokemon2.name}  |  {Player1.Pokemon3.name} ")
                    Player1.Switch_Pokemon(input())
                
    else:
        ########################################################   ATTAQUE DES POKEMONS   ########################################################
        if choixPokemon2 == "attaque":
            Player1.Pokemon_fighting().DamageTaken( Player2.Pokemon_fighting().atkDmg[numAtkPoke2]*Avantage_type( Player2.Pokemon_fighting().type, Player1.Pokemon_fighting().type))
            print(f"{ Player2.Pokemon_fighting().name} attaque { Player1.Pokemon_fighting().name} de ", Player2.Pokemon_fighting().atkDmg[numAtkPoke2]*Avantage_type( Player2.Pokemon_fighting().type, Player1.Pokemon_fighting().type))
            if not ( Player1.Pokemon_fighting().is_alive()):
                print(f"{ Player1.Pokemon_fighting().name} fainted")
                print('---------------------------')
                if Player1.Is_Team_Dead():
                    break
                print(f"{Player1.Pokemon1.name}  |  {Player1.Pokemon2.name}  |  {Player1.Pokemon3.name} ")
                Player1.Switch_Pokemon(input())
                while not(Player1.pokemon_fighting.is_alive()):
                    print(" // This Pokemon is dead pick another one // ")
                    print(f"{Player1.Pokemon1.name}  |  {Player1.Pokemon2.name}  |  {Player1.Pokemon3.name} ")
                    Player1.Switch_Pokemon(input())

        if choixPokemon1 == "attaque":
            Player2.Pokemon_fighting().DamageTaken( Player1.Pokemon_fighting().atkDmg[numAtkPoke1]*Avantage_type( Player1.Pokemon_fighting().type,  Player2.Pokemon_fighting().type))
            print(f"{ Player1.Pokemon_fighting().name} attaque { Player2.Pokemon_fighting().name} de ", Player1.Pokemon_fighting().atkDmg[numAtkPoke1]*Avantage_type( Player1.Pokemon_fighting().type,  Player2.Pokemon_fighting().type))
            if not ( Player2.Pokemon_fighting().is_alive()):
                print(f"{ Player2.Pokemon_fighting().name} fainted")
                print('---------------------------')
                if Player2.Is_Team_Dead():
                    break
                print(f"{Player2.Pokemon1.name}  |  {Player2.Pokemon2.name}  |  {Player2.Pokemon3.name} ")
                Player2.Switch_Pokemon(input())
                while not(Player2.pokemon_fighting.is_alive()):
                    print(f"{Player2.Pokemon1.name}  |  {Player2.Pokemon2.name}  |  {Player2.Pokemon3.name} ")
                    Player2.Switch_Pokemon(input())

    print(f"   -    { Player2.Pokemon_fighting().name} a encore  : ",  Player2.Pokemon_fighting().hp)
    print(f"   -    { Player1.Pokemon_fighting().name} a encore  : ", Player1.Pokemon_fighting().hp)

    
if Player2.Is_Team_Dead():
    print(f"{ Player1.name} gagne ce combat !!")
elif Player1.Is_Team_Dead():
    print(f"{ Player2.name} gagne ce combat !!")

    


