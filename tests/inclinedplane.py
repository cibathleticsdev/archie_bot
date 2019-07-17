from data import *
import math
import discord
import asyncio
import random
import time
import subprocess
import platform

def clear():
    subprocess.Popen("cls" if platform.system() == "Windows" else "clear", shell=True)


# INITIAL SCRIPT #
def initial():
    clear()
    time.sleep(0.01)
    print(Cyan + ' ')
    print('* * * * * * * * * * * * * * * * * * * * * * * * * * *')
    print('* I N C L I N E D   P L A N E   C A L C U L A T O R *')
    print('* * * * * * * * * * * * * * * * * * * * * * * * * * *')
    time.sleep(1)
    print(' ')
    time.sleep(0.1)
    print(' ')
    time.sleep(0.1)
    print('                                                    ***')
    time.sleep(0.1)
    print('                                                 ******')
    time.sleep(0.1)
    print('                                              *********')
    time.sleep(0.1)
    print('                                           ************')
    time.sleep(0.1)
    print('                                         **************')
    time.sleep(0.1)
    print('                                      *****************')
    time.sleep(0.1)
    print('                                   ********************')
    time.sleep(0.1)
    print('                                ***********************')
    time.sleep(0.1)
    print('                             **************************')
    time.sleep(0.1)
    print('                          *****************************')
    time.sleep(0.1)
    print('                       ********************************')
    time.sleep(0.1)
    print('                    ***********************************')
    time.sleep(0.1)
    print('                 **************************************')
    time.sleep(0.1)
    print('              *****************************************')
    time.sleep(0.1)
    print('           ********************************************')
    time.sleep(0.1)
    print('        ***********************************************')
    time.sleep(0.1)
    print('     **************************************************')
    time.sleep(0.1)
    print('  *****************************************************')
    time.sleep(0.1)
    print(' ')
    time.sleep(0.1)
    print(' ')
    time.sleep(0.1)
    print(' ')
    time.sleep(0.1)
    print(' ' + Color_Off)
    time.sleep(1)
    return

def home():
    print(Cyan + 'Press "S" to start calculator, "H" for help or information, "M" to return to the main menu or "E" to exit the program. Then press enter.' + Color_Off)
    home.varinput = input()

    if home.varinput in ['S', 's', 'START', 'start']:
        # INPUT SCRIPT #
        print(Cyan + 'Insert object mass (kg): ' + Color_Off)
        m = eval(input())
        print(Cyan + 'Insert gravity (m/s²): ' + Color_Off)
        g = eval(input())
        print(Cyan + 'Insert plane\'s inclination angel (DEG): ' + Color_Off)
        Â = eval(input())
        print(Cyan + 'Insert coefficient of friction: ' + Color_Off)
        µ = eval(input())

        # CALCULATIONS AND FORMULES #
        P = m * g
        Px = m * g * math.sin(math.radians(Â))
        Py = m * g * math.cos(math.radians(Â))
        N = -Py
        Fƒ = µ * N
        Fres = Px + Fƒ
        a = Fres / m

        # DISPLAY SCRIPT #
        print(' ')
        print(Cyan + 'INPUT' + Color_Off)
        print('m = ' + str(m) + ' kg')
        print('g = ' + str(g) + ' m/s²')
        print('Â = ' + str(Â) + 'º')
        print('µ = ' + str(µ))
        print(' ')
        print(Cyan + 'OUTPUT' + Color_Off)
        print('P = ' + str(P) + ' N')
        print('Px = ' + str(Px) + ' N')
        print('Py = ' + str(Py) + ' N')
        print('N = ' + str(N) + ' N')
        print('Fƒ = ' + str(Fƒ) + ' N')
        print('Fres = ' + str(Fres) + ' N')
        print('a (Fres) = ' + str(a) + ' m/s²')
        time.sleep(3)
        print(' ')
        print(' ')
        home()
        return


    elif home.varinput in ['H', 'h', 'HELP', 'help', 'INFO', 'info', 'I', 'i']:
        from physics import info

    elif home.varinput in ['E', 'e', 'EXIT', 'exit']:
        print('Leaving program')

    elif home.varinput in ['M', 'm', 'MENU', 'menu']:
        import physics

    else:
        print(Red + 'Error, type a valid input' + Color_Off)
        home()

    return

initial()
home()
