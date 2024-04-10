from random import randint
from type import Avantage_type
from items import Items, Def_Items
from player import Player

# Pokemon1 = Pokemon("Dracaufeu", 300, Type.FEU, 250, "Growl", 5, Type.NORMAL, "Ember", 20, Type.FEU)
# Pokemon2 = Pokemon("Tortank", 350, Type.EAU, 100, "Head butt", 10, Type.NORMAL, "Water Canon", 25, Type.EAU)
Players = []
Item_Players = []
Status = "Starting"

choixPokemon1 = None
choixPokemon2 = None

numAtkPoke1 = None
numAtkPoke2 = None
#########################   PLAYER DEFINITION   #########################
def Get_Id_Joueur():
    return str(len(Players) - 1)

def Get_Game_Status():
    return Status

def is_Team_Dead(idJoueur):
    return Players[idJoueur].Is_Team_Dead()

def Use_item(idJoueur, item):
    Item_Players[idJoueur].Use(Def_Items(item))
    return Item_Players[idJoueur].Def_Items(item)

def Def_Player(PlayerName, card1_name, card1_hp, card1_type, card1_nb_attack, card1_attack1_name, card1_attack1_dmg, card1_attack2_name, card1_attack2_dmg, card2_name, card2_hp, card2_type, card2_nb_attack, card2_attack1_name, card2_attack1_dmg, card2_attack2_name, card2_attack2_dmg, card3_name, card3_hp, card3_type, card3_nb_attack, card3_attack1_name, card3_attack1_dmg, card3_attack2_name, card3_attack2_dmg):
    Players.append(Player(PlayerName, card1_name, card1_hp, card1_type, card1_nb_attack, card1_attack1_name, card1_attack1_dmg, card1_attack2_name, card1_attack2_dmg, card2_name, card2_hp, card2_type, card2_nb_attack, card2_attack1_name, card2_attack1_dmg, card2_attack2_name, card2_attack2_dmg, card3_name, card3_hp, card3_type, card3_nb_attack, card3_attack1_name, card3_attack1_dmg, card3_attack2_name, card3_attack2_dmg))
    Item_Players.append(Items(Players[len(Players)-1],1,1,1,1))
    print(Players[len(Players)-1].name, Players[len(Players)-1].Pokemon2.name)

    if len(Players) == 2:
        Status = "Game ready"
    return str(len(Players) - 1)

def Choice(choix, numAtk, idJoueur):
    if idJoueur == 1:
        choixPokemon1 = choix
        numAtkPoke1 = numAtk
    else:
        choixPokemon2 = choix
        numAtkPoke2 = numAtk
    if choixPokemon1 != None and choixPokemon2 != None:
        Status = "Turn ready"
    else:
        Status = "Waiting"
    return Status


def Turn(choixPokemon1, choixPokemon2):
    if randint(1,2) == 1: # CHOI DU JOUEUR PRIORITAIRE
        ########################################################   ATTAQUE DES POKEMONS   ######################################################## '
        if (choixPokemon1 == "attaque" or choixPokemon1 == 'a'):
            Players[1].Pokemon_fighting().DamageTaken( Players[0].Pokemon_fighting().atkDmg[numAtkPoke1]*Avantage_type( Players[0].Pokemon_fighting().type,  Players[1].Pokemon_fighting().type))
            print(f"{ Players[0].Pokemon_fighting().name} attaque { Players[1].Pokemon_fighting().name} de ", Players[0].Pokemon_fighting().atkDmg[numAtkPoke1]*Avantage_type( Players[0].Pokemon_fighting().type,  Players[1].Pokemon_fighting().type))
            if not ( Players[1].Pokemon_fighting().is_alive()):
                if Players[1].Is_Team_Dead():
                    return (f'{Players[1]} is defeated')
                return (f"{ Players[1].Pokemon_fighting().name} fainted")
                # print('---------------------------')
                
                # print(f"{Players[1].Pokemon1.name}  |  {Players[1].Pokemon2.name}  |  {Players[1].Pokemon3.name} ")
                # Players[1].Switch_Pokemon(input())
                # while not(Players[1].pokemon_fighting.is_alive()):
                #     print(f"{Players[1].Pokemon1.name}  |  {Players[1].Pokemon2.name}  |  {Players[1].Pokemon3.name} ")
                #     Players[1].Switch_Pokemon(input())
                
        if (choixPokemon2 == "attaque" or choixPokemon2 == "a"):
            Players[0].Pokemon_fighting().DamageTaken( Players[1].Pokemon_fighting().atkDmg[numAtkPoke2]*Avantage_type( Players[1].Pokemon_fighting().type, Players[0].Pokemon_fighting().type))
            print(f"{ Players[1].Pokemon_fighting().name} attaque { Players[0].Pokemon_fighting().name} de ", Players[1].Pokemon_fighting().atkDmg[numAtkPoke2]*Avantage_type( Players[1].Pokemon_fighting().type, Players[0].Pokemon_fighting().type))
            if not ( Players[0].Pokemon_fighting().is_alive()):
                if Players[0].Is_Team_Dead():
                    return (f'{Players[0]} is defeated')
                return (f"{ Players[0].Pokemon_fighting().name} fainted")
    else:
        ########################################################   ATTAQUE DES POKEMONS   ########################################################
        if (choixPokemon2 == "attaque" or choixPokemon2 == "a"):
            Players[0].Pokemon_fighting().DamageTaken( Players[1].Pokemon_fighting().atkDmg[numAtkPoke2]*Avantage_type( Players[1].Pokemon_fighting().type, Players[0].Pokemon_fighting().type))
            print(f"{ Players[1].Pokemon_fighting().name} attaque { Players[0].Pokemon_fighting().name} de ", Players[1].Pokemon_fighting().atkDmg[numAtkPoke2]*Avantage_type( Players[1].Pokemon_fighting().type, Players[0].Pokemon_fighting().type))
            if not ( Players[0].Pokemon_fighting().is_alive()):
                if Players[0].Is_Team_Dead():
                    return (f'{Players[0]} is defeated')
                return (f"{ Players[0].Pokemon_fighting().name} fainted")

        if (choixPokemon1 == "attaque" or choixPokemon1 == 'a'):
            Players[1].Pokemon_fighting().DamageTaken( Players[0].Pokemon_fighting().atkDmg[numAtkPoke1]*Avantage_type( Players[0].Pokemon_fighting().type,  Players[1].Pokemon_fighting().type))
            print(f"{ Players[0].Pokemon_fighting().name} attaque { Players[1].Pokemon_fighting().name} de ", Players[0].Pokemon_fighting().atkDmg[numAtkPoke1]*Avantage_type( Players[0].Pokemon_fighting().type,  Players[1].Pokemon_fighting().type))
            if not ( Players[1].Pokemon_fighting().is_alive()):
                if Players[1].Is_Team_Dead():
                    return (f'{Players[1]} is defeated')
                return (f"{ Players[1].Pokemon_fighting().name} fainted")
    
    choixPokemon1 = None
    choixPokemon2 = None
    return f"   -    { Players[1].Pokemon_fighting().name} a encore  :   {Players[1].Pokemon_fighting().hp}    -    { Players[0].Pokemon_fighting().name} a encore  :  {Players[0].Pokemon_fighting().hp})"

        

        


