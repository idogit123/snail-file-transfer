from modules.server.server import SocketServer
from modules.ui.ui import UI

def main():
    client = SocketServer()

    while True:
        command = UI.wait_for_command()
        command.run(client)

main()