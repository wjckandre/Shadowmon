import easyocr
import cv2
import os
from pokemontcgsdk import *
import pypokedex as pypo



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
            if n >= 3:
                break
        elif key == ord('q'):
            break

    cv2.destroyWindow(window_name)

def CameraPhotoTexte():
    save_frame_camera_key(0, 'Shadowmon.io/data/temp', 'camera_capture')
    reader = easyocr.Reader(['fr','en'],True) # this needs to run only once to load the model into memory
    # result = reader.readtext('data/temp/camera_capture_0.jpg')
    infos = []
    for x in range(0,3):
        result = reader.readtext(f'Shadowmon.io/data/temp/camera_capture_{x}.jpg')
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
    return infos

def SearchCard(infos):
    cards = Card.where(q=f'name:{infos[0]} hp:{infos[1]} attacks.name:{infos[2]}')
    return cards[0]
def SearchPokemon(infos):
    return pypo.get(name=infos[0])

carte =  SearchPokemon(('deoxys','e'))
print(carte.types[0])