#import modules
import socket
import threading
import flet as ft
import os
from chatapp import Message, ChatMessage
from flask import Flask
from flask_cors import CORS


#localhost=127.0.0.1 et port 3000; test sur wifi IPV4= 192.168.1.16 port 3000
HOST="192.168.1.16"
PORT=3000 #peut utiliser n'importe quel port entre 0 et 65535
LISTENER_LIMIT= 5
CONNEXION =[]
THREAD = []
HEADER = "HTTP/1.1 201 CREATED\r\nContent-Length: 5\r\nHost: localhost:3000\r\nAccess-Control-Allow-Origin: *\r\nContent-Type: text/html; charset=utf-8\r\nBody: Hello\r\n\r\n"
DEFAULT_FLET_PATH = 'http:/localhost'  # or 'ui/path'
DEFAULT_FLET_PORT = 3000
app = Flask(__name__)
CORS(app)


@app.route("/")
#fonction principal
def main(page: ft.Page):
    #creation socket class object
    # AF_INET = utilisation d'addreses IPV4
    # SOCK_STREAM= utilisation de package TCP (communication)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    page.title = "You Enjoy Mychatbot"
    page.add(ft.Text("connecter avec succès"))


#création "try catch block"
    try:
        # fournir au serveur une adresse sous forme de host IP and port
        server.bind((HOST, PORT))
        print(f"Running the server on {HOST}{PORT}")
    except:
        print(f"Unable to bind to host {HOST} and port {PORT}")

    # appliquer server limit
    server.listen(LISTENER_LIMIT)
    # fonction while loop qui continura d'écouter les connections client
    while 1:

        (client, address) = server.accept()
        with client:

            print(client)
            print(address)
            CONNEXION.append([client, address])
            client.send(HEADER.encode())
            #client.close()
            #for i in CONNEXION:
                #i[0].send(f"Bienvenue sur le server {i[1][0]}".encode())
            print(f"connecter avec succès au client{address[0]} {address[1]}")
           # thread= threading.Thread(target=handleclient, args=(client,))
            #THREAD.append(thread)
           # thread.start()
    
    #for p in THREAD:
    p = 0
    while p<len(THREAD):
        THREAD[p].join()
        p+=1
        

def handleclient(client):
    
        while True:
            ct= client.recvfrom(1024)
            for i in CONNEXION:
               
                if i[0] is not client:
                    i[0].send(ct[0])


if __name__=="__main__":
    #main()
    flet_path = os.getenv("FLET_PATH", DEFAULT_FLET_PATH)
    flet_port = int(os.getenv("FLET_PORT", DEFAULT_FLET_PORT))
    ft.app(target=main, view=ft.WEB_BROWSER)
    app.run(host = '192.168.1.16', port = 3000)