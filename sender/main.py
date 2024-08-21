import os
import socket
from easygui import fileopenbox

ADDRESS = ("localhost", 8080)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

file_path: str = fileopenbox()
file = open(file_path, "rb")
file_size = os.path.getsize(file_path)
file_name = os.path.basename(file_path)

client.send(file_name.encode())
client.send(str(file_size).encode())

data = file.read()
client.sendall(data)
client.send(b"<END>")

file.close()
client.close()