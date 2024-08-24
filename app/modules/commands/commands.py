from typing import Any
from modules.server.server import SocketServer
from ..commands.send import send_function
from ..commands.listen import listen_function
from ..commands.exit import exit_function

class Command:
    def __init__(self, name: str, discription: str, function) -> None:
        self.name = name
        self.discription = discription
        self.function = function

    def __str__(self) -> str:
        return f"[{self.name}] {self.discription}"
    
    def run(self, client: SocketServer):
        self.function(client)
    


commands = {
    "send": Command("send", "send file to other computer.", send_function),
    "listen": Command("listen", "listen to incoming send requests.", listen_function),
    "exit": Command("exit", "exit the program.", exit_function)
}