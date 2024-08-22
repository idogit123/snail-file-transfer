import os
import socket
from easygui import fileopenbox

ADDRESS = ("localhost", 8080)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

print(f"connected succesfuly, {client.getsockname()}")
print("please select a file")

file_path: str = fileopenbox()
file = open(file_path, "rb")
file_size = os.path.getsize(file_path)
file_name = os.path.basename(file_path)

client.send(f"{file_name}<NAME>".encode())
client.send(f"{str(file_size)}<SIZE>".encode())

data = file.read()
client.sendall(data)
client.send(b"<FILE>")

print("file sent")

file.close()
client.close()