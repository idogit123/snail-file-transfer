from ..server.server import SocketServer

def exit_function(client: SocketServer):
    client.close()
    exit()