import socket
from recive import Reciver

ADDRESS = ("10.0.0.175", 8080)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)
server.listen()

print(f"listening on {server.getsockname()}")

client, _ = server.accept()
reciver = Reciver(client)

file_name = reciver.recive_til_tag(b"<NAME>").decode()
file_size = reciver.recive_til_tag(b"<SIZE>").decode()

print(f"File: {file_name} has {file_size} bytes.")

reciver.recive_and_write_til_tag(b"<FILE>", file_name)

print("file recived")