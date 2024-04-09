from flask import Flask
from game import Def_Player

app = Flask(__name__)

@app.route('/')
def main():
    return 'tas réussi clément'

@app.route('/createRoom/<idRoom>/<idJoueur>')
def home(idRoom, idJoueur):
    return f'Bienvenue sur le serveur de mon ami de id : {idJoueur} / et de room id : {idRoom} !'

@app.route('/definition_player/<PlayerName>/<card1_name>/<card1_hp>/<card1_type>/<card1_nb_attack>/<card1_attack1_name>/<card1_attack1_dmg>/<card1_attack2_name>/<card1_attack2_dmg>/<card2_name>/<card2_hp>/<card2_type>/<card2_nb_attack>/<card2_attack1_name>/<card2_attack1_dmg>/<card2_attack2_name>/<card2_attack2_dmg>/<card3_name>/<card3_hp>/<card3_type>/<card3_nb_attack>/<card3_attack1_name>/<card3_attack1_dmg>/<card3_attack2_name>/<card3_attack2_dmg>')
def Definition(PlayerName, card1_name, card1_hp, card1_type, card1_nb_attack, card1_attack1_name, card1_attack1_dmg, card1_attack2_name, card1_attack2_dmg, card2_name, card2_hp, card2_type, card2_nb_attack, card2_attack1_name, card2_attack1_dmg, card2_attack2_name, card2_attack2_dmg, card3_name, card3_hp, card3_type, card3_nb_attack, card3_attack1_name, card3_attack1_dmg, card3_attack2_name, card3_attack2_dmg):
    return Def_Player(PlayerName, card1_name, card1_hp, card1_type, card1_nb_attack, card1_attack1_name, card1_attack1_dmg, card1_attack2_name, card1_attack2_dmg, card2_name, card2_hp, card2_type, card2_nb_attack, card2_attack1_name, card2_attack1_dmg, card2_attack2_name, card2_attack2_dmg, card3_name, card3_hp, card3_type, card3_nb_attack, card3_attack1_name, card3_attack1_dmg, card3_attack2_name, card3_attack2_dmg)

@app.route('/game/<idJoueur>/<cardName>')
def game(idJoueur, cardName):
    return cardName

if __name__ == '__main__':
    room = {}
    app.run(host='0.0.0.0', port=5000, debug=True)

