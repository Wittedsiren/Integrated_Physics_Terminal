#This is for running sxp from the terminal.
from bin.tbc import *
import os
import time

command = ""

def commandLine():
    print("Command (tpye 'help' for assitance):")
    command = input()
    try:
        listOfCommands[str.lower(command)]()
    except ValueError:
        print("That is not a command found in SXP database. Try typing 'help' for a list of commands")

    commandLine()

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

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
startUp()