from data import *
import math
import discord
import asyncio
import random
import time


print(Cyan + '* * * * * * * * * * * * * * * * * * * * * * * * * * *')
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

def home():
    print(Cyan + 'Press "S" to start calculator, "H" for help or information or "E" to exit the program. Then press enter.' + Color_Off)
    home.varinput = input()

    if home.varinput in ['S', 's', 'START', 'start']:
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


    elif home.varinput in ['H', 'h', 'HELP', 'help', 'INFO', 'info']:
        print(UCyan + 'What is inclined-plane calculator?')
        print(Cyan + 'This software can calculate almost all forces and some accelerations acting in the inclined plane. You just have to introduce the mass, gravity, inclination angle and coefficient of friction.' + Color_Off)
        input("Press any key to continue...")
        home()

    elif home.varinput in ['E', 'e', 'EXIT', 'exit']:
        print('exit')

    else:
        print('ERROR, ABORTING')

    return


home()
