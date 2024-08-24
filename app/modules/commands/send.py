from ..server.server import SocketServer
from os.path import getsize, basename

def send_function(client: SocketServer):
    from ..ui.ui import UI
    # 2: Connect to reciver
    reciver_IP = UI.ask_for("Enter the IP of the reciver computer.")
    reciver_port = int(UI.wait_for(
        "Enter the port of the reciver computer.", 
        str.isdigit,
        not_valid_msg="Invalid port number."
    ))
    client.connect((reciver_IP, reciver_port))

    # 3: Send file metadata
    file_path = UI.ask_for_file(
        "Select a file to send in the 'Select File' window.",
        "Select a file to send.",
        "Select File"
    )
    file_name: str = basename(file_path)
    file_size = getsize(file_path)
    file_metadata = file_name.encode() + b';' + str(file_size).encode()
    client.send_tag(file_metadata, b"<METADATA>")