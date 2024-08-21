import socket

ADDRESS = ("localhost", 8080)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)
server.listen()

client, _ = server.accept()

file_name = client.recv(1024).decode()
file_size = client.recv(1024).decode()



print(f"File: {file_name} has {file_size} bytes.")