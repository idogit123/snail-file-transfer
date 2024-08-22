import socket

class SocketServer:
    def __init__(self, port = 8080) -> None:
        self.HOST_NAME = socket.gethostname()
        self.HOST_IP = socket.gethostbyname(self.HOST_NAME)
        self.ADDRESS = (self.HOST_IP, port)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.server.bind(self.ADDRESS)
        print(f"[BIND] Server is bound to {self.ADDRESS}")
        

    def connect(self, address):
        self.server.connect(address)
        print(f"[CONNECT SUCCEED] Succesfuly connected to {address}")

    def accept(self):
        self.server.listen()
        print(f"[LISTENING] Server listening on {self.ADDRESS}")
        client, client_address = self.server.accept()
        print(f"[ACCEPT] Accepted connection from {client_address}")

        return client, client_address
    
    def close(self):
        self.server.close()
        print("[CLOSED] Server closed.")