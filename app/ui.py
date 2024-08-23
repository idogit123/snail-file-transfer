from commands import commands

class UI:
    def welcome():
        print("Welcome to Snail File Transfer!")

    def print_commands():
        for command in commands:
            print(command)

    def ask_for_command():
        print("Enter command: ")
        UI.print_commands()
        return input("--> ")

    def wait_for_command():
        print()
        command = UI.ask_for_command()
        while not command in commands.keys():
            print("[ERROR] Command not found!")
            command = UI.ask_for_command()

        return commands.get(command)
