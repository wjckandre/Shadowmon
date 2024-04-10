from flask import Flask
from game import Get_Id_Joueur, Get_Game_Status, Def_Player, Players, Item_Players, Use_item, Choice, Turn, choixPokemon1, choixPokemon2

app = Flask(__name__)

@app.route('/')
def main():
    return 'tas réussi clément'

@app.route('/createRoom/<idRoom>/<idJoueur>')
def home(idRoom, idJoueur):
    return f'Bienvenue sur le serveur de mon ami de id : {idJoueur} / et de room id : {idRoom} !'

@app.route('/definition_player/<PlayerName>/<card1_name>/<card1_hp>/<card1_type>/<card1_nb_attack>/<card1_attack1_name>/<card1_attack1_dmg>/<card1_attack2_name>/<card1_attack2_dmg>/<card2_name>/<card2_hp>/<card2_type>/<card2_nb_attack>/<card2_attack1_name>/<card2_attack1_dmg>/<card2_attack2_name>/<card2_attack2_dmg>/<card3_name>/<card3_hp>/<card3_type>/<card3_nb_attack>/<card3_attack1_name>/<card3_attack1_dmg>/<card3_attack2_name>/<card3_attack2_dmg>')
def Definition(PlayerName, card1_name, card1_hp, card1_type, card1_nb_attack, card1_attack1_name, card1_attack1_dmg, card1_attack2_name, card1_attack2_dmg, card2_name, card2_hp, card2_type, card2_nb_attack, card2_attack1_name, card2_attack1_dmg, card2_attack2_name, card2_attack2_dmg, card3_name, card3_hp, card3_type, card3_nb_attack, card3_attack1_name, card3_attack1_dmg, card3_attack2_name, card3_attack2_dmg):
    Def_Player(PlayerName, card1_name, card1_hp, card1_type, card1_nb_attack, card1_attack1_name, card1_attack1_dmg, card1_attack2_name, card1_attack2_dmg, card2_name, card2_hp, card2_type, card2_nb_attack, card2_attack1_name, card2_attack1_dmg, card2_attack2_name, card2_attack2_dmg, card3_name, card3_hp, card3_type, card3_nb_attack, card3_attack1_name, card3_attack1_dmg, card3_attack2_name, card3_attack2_dmg)
    return Get_Id_Joueur()


@app.route("/get_status")
def Status():
    return Get_Game_Status()

@app.route("/is_Team_dead/<idJoueur>")
def is_Team_Dead(idJoueur):
    return is_Team_Dead(idJoueur)

@app.route("/get_name_PokemonFighting/<idJoueur>")
def get_name_PokemonFighting(idJoueur):
    return Players[idJoueur].name

@app.route("get_name_Pokemons/<idJoueur>")
def get_name_Pokemons(idJoueur):
    return [Players[idJoueur].Pokemon1.name, Players[idJoueur].Pokemon2.name , Players[idJoueur].Pokemon3.name]

@app.route("/get_Player_name/<idJoueur>")
def get_Player_name(idJoueur):
    return Players[idJoueur].name

@app.route("/get_hp_PokemonFighting/<idJoueur>")
def get_hp_PokemonFighting(idJoueur):
    return str(Players[idJoueur].hp)

@app.route("/get_name_Atk/<idJoueur>/<idAtk>")
def get_name_Atk(idJoueur, idAtk):
    return Players[idJoueur].pokemon_fighting.atkNom[idAtk]

@app.route("/get_dmg_Atk/<idJoueur>/<idAtk>")
def get_dmg_Atk(idJoueur, idAtk):
    return str(Players[idJoueur].pokemon_fighting.atkDmg[idAtk])

@app.route("/get_nb_items/<idJoueur>")
def get_nb_items(idJoueur):
    return [Item_Players[idJoueur].potions, Item_Players[idJoueur].super_potions, Item_Players[idJoueur].hyper_potions, Item_Players[idJoueur].revive]

@app.route("/Use_items/<idJoueur>/<item>") 
def Use_items(idJoueur, item):
    return Use_item(idJoueur, item)

@app.route("/switch_pokemon/<idJoueur>/<PokemonName>")
def switch_pokemon(idJoueur, PokemonName):
    return Players[idJoueur].Switch_Pokemon(PokemonName)

@app.route("/is_PokemonFighting_alive/<idJoueur>")
def is_PokemonFighting_alive(idJoueur):
    return Players[idJoueur].pokemon_fighting.is_alive()

@app.route("/send_choice/<idJoueur>/<atk>/<numAtk>")
def send_choice(idJoueur, atk, numAtk):
    return Choice(atk, numAtk, idJoueur)

@app.route("/turn") 
def turn():
    return Turn(choixPokemon1, choixPokemon2)


if __name__ == '__main__':
    room = {}
    app.run(host='0.0.0.0', port=5000, debug=True)

