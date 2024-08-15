import os
import socket

ADDRESS = ("localhost", 8080)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

file = open("test.txt", "rb")
file_size = os.path.getsize("test.txt")

client.send("test.txt".encode())
client.send(str(file_size).encode())

data = file.read()
client.sendall(data)
client.send(b"<END>")

file.close()
client.close()