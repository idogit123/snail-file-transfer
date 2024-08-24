from socket import socket
from os.path import getsize, basename

class Sender:

    def send_tag(client: socket, data: bytes, tag: bytes):
        client.send(data + tag)

    def send_file(client: socket, file_path: str):
        with open(file_path, 'rb') as file:
            file_bytes = file.read()
            client.sendall(file_bytes)
