import requests
import easyocr
import cv2
import os
from pokemontcgsdk import *
import pypokedex as pypo
import time as tm
import re



idRoom = 1
ipconfig = "192.168.2.197"
# a = requests.get(f'http://10.10.138.59:5000/createRoom/{idRoom}/{idJoueur}').text
# b = requests.get('http://10.10.138.59:5000/').text

# print(a)
# print(b)




RestClient.configure('12345678-1234-1234-1234-123456789ABC')

def save_frame_camera_key(device_num, dir_path, basename, ext='jpg', delay=1, window_name='frame'):
    cap = cv2.VideoCapture(device_num)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    n = 0
    while True:
        ret, frame = cap.read()
        cv2.imshow(window_name, frame)
        key = cv2.waitKey(delay) & 0xFF
        if key == ord('c'):
            cv2.imwrite('{}_{}.{}'.format(base_path, n, ext), frame)
            n += 1
            print(f"capture n°{n} taken")
            if n >= 3:
                break
        elif key == ord('q'):
            break

    cv2.destroyWindow(window_name)

def CameraPhotoTexte():
    save_frame_camera_key(1, 'data/temp', 'camera_capture')
    reader = easyocr.Reader(['fr','en'],True) # this needs to run only once to load the model into memory
    # result = reader.readtext('data/temp/camera_capture_0.jpg')
    infos = []
    for x in range(0,3):
        result = reader.readtext(f'data/temp/camera_capture_{x}.jpg')
        # print(result)
        # print('name : ',result[0][1] , '| hp : ', result[1][1], ' | first attack : ', result[2][1])
        min = result[0][0][0][1]
        idmin = 0
        for i in range(len(result)):
            # print(result[i][1])
            if min > result[i][0][0][1]:
                min = result[i][0][0][1]
                idmin = i
        chaine = result[idmin][1]
        index_espace = chaine.find(' ')  # Trouver l'index du premier espace
        # print(index_espace)
        if index_espace != -1:  # Vérifier si un espace a été trouvé
            chaine = chaine[:index_espace]  # Extraire tout avant le premier espace
        infos.append(chaine)
    # print(infos)
    return infos

def SearchCard(infos):
    cards = Card.where(q=f'name:{infos[0]} hp:{infos[1]} attacks.name:{infos[2]}')
    return cards[0]
def SearchPokemon(infos):
    return pypo.get(name=infos[0])


def Switch():
    pokemons = requests.get(f'http://{ipconfig}:5000/get_name_Pokemons/{idJoueur}').text
    print(f"{pokemons[0]}  |  {pokemons[1]}  |  {pokemons[2]} ")
    switch = input()
    print(f" Le pokemon au combat est {requests.get(f'http://{ipconfig}:5000/switch_pokemon/{idJoueur}/{switch}').text}")
    while not(requests.get(f'http://{ipconfig}:5000/is_PokemonFighting_alive/{idJoueur}').text == "True"):
        print(" // Mais ce Pokemon est mort veuillez en choisir un autre // ")
        print(f"{pokemons[0]}  |  {pokemons[1]}  |  {pokemons[2]} ")
        switch = input()
        print(f" Le pokemon au combat est {requests.get(f'http://{ipconfig}:5000/switch_pokemon/{idJoueur}/{switch}').text}")

# txt1 = CameraPhotoTexte()
txt1 = ["Petilil", "50", "Ram"]
print(txt1)
carte1 = SearchCard(txt1)
pokemon1 = SearchPokemon(txt1)

print(pokemon1.types)
# txt2 = CameraPhotoTexte()
txt2 = ["Dialga", "130", "Chrono"]
print(txt2)
carte2 = SearchCard(txt2)
pokemon2 = SearchPokemon(txt2)
print(pokemon2.types)

# txt3 = CameraPhotoTexte()
txt3 = ["Tinkatink", "70" ,"Boundless"]
print(txt3)
carte3 = SearchCard(txt3)
pokemon3 = SearchPokemon(txt3)


Player_name = input("Entrez votre nom de joueur : ")
cartes_name = []
cartes_hp = []
cartes_type = []
cartes_nb_attacks = []
cartes_attacks_name = []
cartes_attacks_dmg = []

attacksName = []
attacksDmg = []
for x in range (0, len(carte1.attacks)):
    attacksName.append(carte1.attacks[x].name)
    attacksDmg.append(int(carte1.attacks[x].damage))
attacksName.append(carte1.attacks[len(carte1.attacks)-1].name)
attacksDmg.append(int(carte1.attacks[len(carte1.attacks)-1].damage))
cartes_attacks_name.append(attacksName)
cartes_attacks_dmg.append(attacksDmg)
cartes_name.append(carte1.name)
cartes_hp.append(int(carte1.hp))
cartes_type.append(pokemon1.types[0])
cartes_nb_attacks.append(len(carte1.attacks)-1)

attacksName = []
attacksDmg = []
for x in range (0, len(carte2.attacks)):
    attacksName.append(carte2.attacks[x].name)
    attacksDmg.append(int(carte2.attacks[x].damage))
attacksName.append(carte2.attacks[len(carte2.attacks)-1].name)
attacksDmg.append(int(carte2.attacks[len(carte2.attacks)-1].damage))
cartes_attacks_name.append(attacksName)
cartes_attacks_dmg.append(attacksDmg)
cartes_name.append(carte2.name)
cartes_hp.append(int(carte2.hp))
cartes_type.append(pokemon2.types[0])
cartes_nb_attacks.append(len(carte2.attacks)-1)

attacksName = []
attacksDmg = []
for x in range (0, len(carte3.attacks)):
    attacksName.append(carte3.attacks[x].name)
    attacksDmg.append(int(carte3.attacks[x].damage))
attacksName.append(carte3.attacks[len(carte3.attacks)-1].name)
attacksDmg.append(int(carte3.attacks[len(carte3.attacks)-1].damage))
cartes_attacks_name.append(attacksName)
cartes_attacks_dmg.append(attacksDmg)
cartes_name.append(carte3.name)
cartes_hp.append(int(carte3.hp))
cartes_type.append(pokemon3.types[0])
cartes_nb_attacks.append(len(carte3.attacks)-1)


print(cartes_name)
idJoueur = requests.get(f'http://{ipconfig}:5000/definition_player/{Player_name}/{cartes_name[0]}/{cartes_hp[0]}/{cartes_type[0]}/{cartes_nb_attacks[0]}/{cartes_attacks_name[0][0]}/{cartes_attacks_dmg[0][0]}/{cartes_attacks_name[0][1]}/{cartes_attacks_dmg[0][1]}/{cartes_name[1]}/{cartes_hp[1]}/{cartes_type[1]}/{cartes_nb_attacks[1]}/{cartes_attacks_name[1][0]}/{cartes_attacks_dmg[1][0]}/{cartes_attacks_name[1][1]}/{cartes_attacks_dmg[1][1]}/{cartes_name[2]}/{cartes_hp[2]}/{cartes_type[2]}/{cartes_nb_attacks[2]}/{cartes_attacks_name[2][0]}/{cartes_attacks_dmg[2][0]}/{cartes_attacks_name[2][1]}/{cartes_attacks_dmg[2][1]}').json()
print(idJoueur)
if idJoueur == 0:
    idAdversaire = 1
else:
    idAdversaire = 0


while requests.get(f'http://{ipconfig}:5000/get_status').text == "Starting":
    print("Waiting For Other Player")
    tm.sleep(3)

nbTours = 0
while requests.get(f'http://{ipconfig}:5000/get_status').text != "Game finished":
    nbTours += 1

    while requests.get(f'http://{ipconfig}:5000/get_status').text == "Starting":
        print("Waiting For Other Player")
        tm.sleep(2)

    print('---------------------------')
    print("Début du tours  :  ", nbTours)
    print('---------------------------')
    print(f" Choisissez l'action de { requests.get(f'http://{ipconfig}:5000/get_name_PokemonFighting/{idJoueur}').text} : ")
    print("-----------------------------------------")
    print("|                   |                   |")
    print("|     ATTAQUE       |       SOINS       |")
    print("|                   |                   |")
    print("-----------------------------------------")
    print("|                   |                   |")
    print("|     POKEMON       |        FUIR       |")
    print("|                   |                   |")
    print("-----------------------------------------")
    choix = input()
    if choix == "attaque" or choix == "a":
        numAtkPoke1 = int(input(f"Numéro de l'attaque choisie pour { requests.get(f'http://{ipconfig}:5000/get_name_PokemonFighting/{idJoueur}').text} :  (1) { requests.get(f'http://{ipconfig}:5000/get_name_Atk/{idJoueur}/{0}').text} / { requests.get(f'http://{ipconfig}:5000/get_dmg_Atk/{idJoueur}/{0}').json()}  (2) {requests.get(f'http://{ipconfig}:5000/get_name_Atk/{idJoueur}/{1}').text} / { requests.get(f'http://{ipconfig}:5000/get_dmg_Atk/{idJoueur}/{1}').json()}   : ")) - 1
        while numAtkPoke1 != 0 and numAtkPoke1 != 1:
            numAtkPoke1 = int(input(f"Numéro de l'attaque choisie pour { requests.get(f'http://{ipconfig}:5000/get_name_PokemonFighting/{idJoueur}').text} :  (1) { requests.get(f'http://{ipconfig}:5000/get_name_Atk/{idJoueur}/{0}').text} / { requests.get(f'http://{ipconfig}:5000/get_dmg_Atk/{idJoueur}/{0}').json()}  (2) {requests.get(f'http://{ipconfig}:5000/get_name_Atk/{idJoueur}/{1}').text} / { requests.get(f'http://{ipconfig}:5000/get_dmg_Atk/{idJoueur}/{1}').json()}   : ")) - 1
    elif choix == "soins" or choix == "s":
        items = requests.get(f'http://{ipconfig}:5000/get_nb_items/{idJoueur}').json()
        print(f" Potions : {items[0]} |  Super Potions : {items[1]} |  Hyper Potions : {items[2]} |  Revive : {items[3]}")
        nom_item = input()
        print(f"Vous avez utilisé un(e) {requests.get(f'http://{ipconfig}:5000/Use_items/{idJoueur}/{nom_item}').text}")
    elif choix == "pokemon" or choix == "p":
        
        pokemons = requests.get(f'http://{ipconfig}:5000/get_name_Pokemons/{idJoueur}').json()
        print(f"{pokemons[0]}  |  {pokemons[1]}  |  {pokemons[2]} ")
        switch = input()
        print(f" Le pokemon au combat est {requests.get(f'http://{ipconfig}:5000/switch_pokemon/{idJoueur}/{switch}').text}")
        while not(requests.get(f'http://{ipconfig}:5000/is_PokemonFighting_alive/{idJoueur}').text == "True"):
            print(" // Mais ce Pokemon est mort veuillez en choisir un autre // ")
            print(f"{pokemons[0]}  |  {pokemons[1]}  |  {pokemons[2]} ")
            switch = input()
            print(f" Le pokemon au combat est {requests.get(f'http://{ipconfig}:5000/switch_pokemon/{idJoueur}/{switch}').text}")
        
    else:
        print(f"{Player_name} flew away !  {requests.get(f'http://{ipconfig}:5000/get_Player_name/{idAdversaire}').text} won the battle")
        break
    if choix != 'attaque' or choix != "a":
        numAtkPoke1 = 0
    requests.get(f'http://{ipconfig}:5000/send_choice/{idJoueur}/{choix}/{numAtkPoke1}').text
    while requests.get(f'http://{ipconfig}:5000/get_status').text == "Waiting":
        print("Waiting For Other Player")
        tm.sleep(2)
    response = (requests.get(f'http://{ipconfig}:5000/turn').text)
   
    if re.search("defeated",response):
        if re.search(f"{Player_name}",response):
            print("Votre adversaire gagne ce combat !")
            break
        else:
            print(" Vous gagnez ce combat !")
            break
    elif re.search("fainted", response):
        
        if re.search(f"{requests.get(f'http://{ipconfig}:5000/get_name_PokemonFighting/{idJoueur}').text}", response):
            print(response)
            pokemons = requests.get(f'http://{ipconfig}:5000/get_name_Pokemons/{idJoueur}').json()
            print(f"{pokemons[0]}  |  {pokemons[1]}  |  {pokemons[2]} ")
            switch = input()
            print(f" Le pokemon au combat est {requests.get(f'http://{ipconfig}:5000/switch_pokemon/{idJoueur}/{switch}').text}")
            print("Set status :   ", requests.get(f'http://{ipconfig}:5000/set_Status/Choice_ready').text )
            while not(requests.get(f'http://{ipconfig}:5000/is_PokemonFighting_alive/{idJoueur}').text == "True"):
                print(" // Mais ce Pokemon est mort veuillez en choisir un autre // ")
                print(f"{pokemons[0]}  |  {pokemons[1]}  |  {pokemons[2]} ")
                switch = input()
                print(f" Le pokemon au combat est {requests.get(f'http://{ipconfig}:5000/switch_pokemon/{idJoueur}/{switch}').text}")
                print("Set status :   ", requests.get(f'http://{ipconfig}:5000/set_Status/Choice_ready').text )
        else:
            print("Le pokemon adverse est KO")
    else:
        print(response)

    while not (requests.get(f'http://{ipconfig}:5000/get_status').text == "Choice_ready") :
        tm.sleep(2)
        print("Status : ", requests.get(f'http://{ipconfig}:5000/get_status').text)
        print("Waiting for other player")
    
    
