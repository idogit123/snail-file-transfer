from ..server.server import SocketServer

def listen_function(client: SocketServer):
    from ..ui.ui import UI
    client.accept()
    print(client.recive_tag(b"<REQUEST>"))