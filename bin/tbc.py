#terminal based commands.
from bin.vector import *
import os
def help():
    print("""
type "vector" for vector operation
type "open" to open the SXP window
tpye "math" for basic calculations
""")

def defvector():
    print("\nhow many dimensions?")
    d = input()
    if d.isnumeric() :
        d = int(d)
        vA = vector(d)
        #vector created
        print("\nWhat kind of operation? If you need a list just type 'list'")
        response = input()
        if response.lower() == "list":
            print(operationsList)
            response = input()
        else:
            vectorOperations[response](vA)


    else:
        print("please enter a number")
        defvector()

def mathOp():
    print("Type you calculations below:\n")
    calc = input()
    print(eval(calc))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def version():
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
    print("version 1.0.0")
    print("last update: 14-09-2024")
    print("Open Source\n")

listOfCommands = {
    "help" : help,
    "vector" : defvector,
    "math" : mathOp,
    "clear" : clear,
    "version" : version,
}
