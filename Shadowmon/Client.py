#import modules
import socket
import threading
import flet as ft
import os
from chatapp import Message, ChatMessage
from flask import Flask
from flask_cors import CORS

#localhost=127.0.0.1 et port 3000; IPV4= 192.168.1.16 port 5000
HOST = "192.168.1.16"
PORT = 3000
DEFAULT_FLET_PATH = 'http:/localhost'  # or 'ui/path'
DEFAULT_FLET_PORT = 3000
app = Flask(__name__)
CORS(app)


@app.route("/")
#main fonction
def main(page: ft.Page):
    print("main")
    #création object socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    page.title = "You Enjoy Mychatbot"
    page.add(ft.Text("connecter avec succès"))

    #connect au serveur
    try:
        client.connect((HOST, PORT))
        print(f"Successfully connected to server")
        n_client =client.recv(1024)
        print(n_client.decode())
        while n_client:
            message = input("Entrez votre message")
            
            client.send(message.encode())
           
            n_client =client.recv(1024)
            print(n_client.decode())
    except:
        print(f"Unable to connect to server {HOST}{PORT}")

    





if __name__=="__main__":
    #main()
    flet_path = os.getenv("FLET_PATH", DEFAULT_FLET_PATH)
    flet_port = int(os.getenv("FLET_PORT", DEFAULT_FLET_PORT))
    ft.app(target=main, view=ft.WEB_BROWSER)
    app.run(host = '192.168.1.16', port = 3000)