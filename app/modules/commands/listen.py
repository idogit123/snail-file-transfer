from ..server.server import SocketServer

def listen_function(client: SocketServer):
    from ..ui.ui import UI

    # 1: Listen
    client.accept()

    # 3: Recive file metadata
    file_name, file_size = client.recive_tag(b"<METADATA>").decode().split(';')
    print(f"Send request recived: File: {file_name}, Size: {file_size} bytes.")

    # 4: Accept / Deny request
    is_accepted = bool(UI.wait_for(
        "Do you want to accept the request?",
        lambda answer: answer in ["True", "False"],
        print_options=lambda: print("Enter [True] to accept or [False] to deny the request.")
    ))
    client.send_tag(str(is_accepted).encode(), b"<ACCEPT>")

    # 5: If request denyed, exit
    if not is_accepted:
        print("[REJECTED] You rejected the request.")
        return False


    