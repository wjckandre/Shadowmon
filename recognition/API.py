import easyocr
import cv2
import os
from pokemontcgsdk import *


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
            break
        elif key == ord('q'):
            break

    cv2.destroyWindow(window_name)


# save_frame_camera_key(0, 'data/temp', 'camera_capture')
reader = easyocr.Reader(['fr','en'],True) # this needs to run only once to load the model into memory
result = reader.readtext('data/temp/camera_capture_0.jpg')
# result = reader.readtext('ok.jpg')
print(result)
# print('name : ',result[0][1] , '| hp : ', result[1][1], ' | first attack : ', result[2][1])
min = result[0][0][0][0]
idmin = 0
for i in range(len(result)):
    print(result[i][1])
    if min > result[i][0][0][0]:
        min = result[i][0][0][0]
        idmin = i

infos = (result[idmin][1] , result[0][1] , result[1][1])
print( infos)
# cards = Card.where(q=f'name:{result[0][1]} hp:{result[1][1]} attacks.name:{result[2][1]}')
# print(cards[0])