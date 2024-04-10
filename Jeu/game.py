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
    return choixPokemon1 != None and choixPokemon2 != None


def Turn():
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

        


