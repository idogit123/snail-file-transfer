from ..commands.commands import commands, Command
from typing import Any, Callable
from easygui import fileopenbox, filesavebox

class UI:
    def welcome():
        print("Welcome to Snail File Transfer!")

    def print_commands():
        for command in commands:
            print(command)
    
    def ask_for(instruction: str, print_options = None) -> str:
        print(instruction)
        if print_options != None:
            print_options()

        return input ('--> ')
    
    def wait_for(instruction: str, is_valid, print_options = None, not_valid_msg = "Answer invalid!"):
        answer = UI.ask_for(instruction, print_options=print_options)
        while not is_valid(answer):
            print(f"[ERROR] {not_valid_msg}")
            answer = UI.ask_for(instruction, print_options=print_options)

        return answer


    def wait_for_command() -> Command:
        print()
        command = UI.ask_for("Enter command: ", print_options=UI.print_commands)
        while not command in commands.keys():
            print("[ERROR] Command not found!")
            command = UI.ask_for("Enter command: ", print_options=UI.print_commands)

        return commands.get(command)
    
    def ask_for_file(console_msg: str, msg: str | None = None, title: str | None = None) -> str:
        print(f"[OPEN FILE] {console_msg}")
        return fileopenbox(msg, title, multiple=False)

    def ask_for_save_path(console_msg: str, msg: str | None = None, title: str | None = None, file_name: str | None = None):
        print(f"[SAVE FILE] {console_msg}")
        return filesavebox(msg=msg, title=title, default=file_name)