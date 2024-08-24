from ..server.server import SocketServer

def send_function(client: SocketServer):
    from ..ui.ui import UI
    reciver_IP = UI.ask_for("Enter the IP of the reciver computer.")
    reciver_port = int(UI.wait_for(
        "Enter the port of the reciver computer.", 
        str.isdigit,
        not_valid_msg="Invalid port number."
    ))
    client.connect((reciver_IP, reciver_port))
    client.send_tag(b"Hello World!", b"<REQUEST>")