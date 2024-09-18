#This is for running sxp from the terminal.
from bin.tbc import *
from bin.vectorTerminal import vectorTerminal
import os
import time
import sys

command = ""

def commandLine():
    print("Command (tpye 'help' for assitance):")
    command = input()
    try:
        listOfCommands[str.lower(command)]()
    except ValueError:
        print("That is not a command found in SXP database. Try typing 'help' for a list of commands")
    commandLine()


def startUp():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Initializing IPT...")
    # for i, item in enumerate(items):
    # # Do stuff...
    # time.sleep(0.1)
    # # Update Progress Bar
    # printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    print("""
██╗███╗░░██╗████████╗███████╗░██████╗░██████╗░░█████╗░████████╗███████╗██████╗░
██║████╗░██║╚══██╔══╝██╔════╝██╔════╝░██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██║██╔██╗██║░░░██║░░░█████╗░░██║░░██╗░██████╔╝███████║░░░██║░░░█████╗░░██║░░██║
██║██║╚████║░░░██║░░░██╔══╝░░██║░░╚██╗██╔══██╗██╔══██║░░░██║░░░██╔══╝░░██║░░██║
██║██║░╚███║░░░██║░░░███████╗╚██████╔╝██║░░██║██║░░██║░░░██║░░░███████╗██████╔╝
╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░
          
██████╗░██╗░░░██╗██╗░░██╗░██████╗██╗░█████╗░░██████╗
██╔══██╗╚██╗░██╔╝██║░░██║██╔════╝██║██╔══██╗██╔════╝
██████╔╝░╚████╔╝░███████║╚█████╗░██║██║░░╚═╝╚█████╗░
██╔═══╝░░░╚██╔╝░░██╔══██║░╚═══██╗██║██║░░██╗░╚═══██╗
██║░░░░░░░░██║░░░██║░░██║██████╔╝██║╚█████╔╝██████╔╝
╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░╚═════╝░

████████╗███████╗██████╗░███╗░░░███╗██╗███╗░░██╗░█████╗░██╗░░░░░
╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║████╗░██║██╔══██╗██║░░░░░
░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║██╔██╗██║███████║██║░░░░░
░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║██║╚████║██╔══██║██║░░░░░
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║██║░╚███║██║░░██║███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝                     
""")
    commandLine()




if len(sys.argv) <= 1:
    print("\n--------------------------------------------------\n")
    print("  type 'ipt -help' for help or a list of options")
    print("\n--------------------------------------------------\n")

        
elif sys.argv[1] == "open":
    startUp()
elif sys.argv[1] == "vector":
    vectorTerminal(sys.argv[2])

    