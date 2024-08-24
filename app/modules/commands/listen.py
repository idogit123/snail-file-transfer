from ..server.server import SocketServer

def listen_function(client: SocketServer):
    from ..ui.ui import UI

    # 1: Listen
    client.accept()

    # 3: Recive file metadata
    file_name, file_size = client.recive_tag(b"<METADATA>").decode().split(';')
    print(f"Send request recived: File: {file_name}, Size: {file_size} bytes.")