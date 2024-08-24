from ..server.server import SocketServer

def listen_function(client: SocketServer):
    from ..ui.ui import UI

    # 1: Listen
    client.accept()

    # 3: Recive file metadata
    file_metadata = client.recive_tag(b"<METADATA>").decode().split(';')
    file_name = file_metadata[0]
    file_size = int(file_metadata[1])
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

    # 6: If approved, recive file
    file_bytes = client.recive_file(file_size)
    print("[RECIVED] File recived.")

    # 7: Save file
    file_save_path: str = UI.ask_for_save_path(
        "Select save location for the file in the 'Save File' window.",
        title="Save File",
        file_name=file_name
    )
    with open(file_save_path, 'wb+') as file:
        file.write(file_bytes)