import os
import sys
import datetime
from program import *


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def add_programs_to_path():
    path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(path, "program")
    sys.path.append(path)

    global programs
    programs = []

    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)
        if os.path.isfile(filepath) and filename.endswith(".py"):
            programs.append(filename[:-3])

    return programs


def menu():
    """Display the menu and allow the user to launch a program."""

    global programs

    # Print the menu options
    print("=== Menu ===")
    for i in range(len(programs)):
        print(f"{i + 1} - {programs[i]}")

    # Get the user's choice
    choice = int(input("Enter your choice: "))

    # Launch the selected program
    if 1 <= choice <= len(programs):
        program_name = programs[choice - 1]
        program_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "program", f"{program_name}.py"
        )
        exec(open(program_path, "r").read())
        sys.exit()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    add_programs_to_path()
    clear_console()
    menu()
