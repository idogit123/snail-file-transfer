import os
import socket
from socket import _Address
from easygui import fileopenbox
from time import sleep

class SocketServer:
    def __init__(self, port = 8080) -> None:
        self.HOST_NAME = socket.gethostname()
        self.HOST_IP = socket.gethostbyname(self.HOST_NAME)
        self.ADDRESS = (self.HOST_IP, port)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.server.bind(self.ADDRESS)
        self.server.listen()
        print(f"[LISTENING] Server listening on {self.ADDRESS}")

    def connect(self, address: _Address):
        try:
            self.server.connect(address)
        except:
            print(f"[CONNECT FAILD] Faild to connect to {address}")

        print(f"[CONNECT SUCCEED] Succesfuly connected to {address}")

    def accept(self):
        client, client_address = self.server.accept()
        print(f"[ACCEPT] Accepted connection from {client_address}")

        return client, client_address
    

server = SocketServer()