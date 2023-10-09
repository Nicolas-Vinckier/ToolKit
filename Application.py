import os
import sys
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
    # print(f"{len(programs)} program(s) available")
    print("=== Menu ===")
    for i in range(len(programs)):
        print(f"{i + 1} - {programs[i]}")


add_programs_to_path()
clear_console()
menu()
