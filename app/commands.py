

class Command:
    def __init__(self, name: str, discription: str, function) -> None:
        self.name = name
        self.discription = discription
        self.function = function

    def __str__(self) -> str:
        return f"[{self.name}] {self.discription}"
    
    def run(self):
        self.function()
    
commands = {
    "send": Command("send", "send file to other computer.", lambda: print("[SENDING] Sending file.")),
    "exit": Command("exit", "exit the program.", lambda: exit())
}