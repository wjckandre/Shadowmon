from flask import Flask
from game import Def_Player

app = Flask(__name__)

@app.route('/')
def main():
    return 'tas réussi clément'

@app.route('/createRoom/<idRoom>/<idJoueur>')
def home(idRoom, idJoueur):
    return f'Bienvenue sur le serveur de mon ami de id : {idJoueur} / et de room id : {idRoom} !'

@app.route('/definition_player/<PlayerName>/<txt1>/<carte1>/<txt2>/<carte2>/<txt3>/<carte3>')
def Definition(PlayerName, txt1, carte1, txt2, carte2, txt3, carte3):
    return Def_Player(PlayerName, txt1, carte1, txt2, carte2, txt3, carte3)

@app.route('/game/<idJoueur>/<cardName>')
def game(idJoueur, cardName):
    return cardName

if __name__ == '__main__':
    room = {}
    app.run(host='0.0.0.0', port=5000, debug=True)

