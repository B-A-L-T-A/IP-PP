#Programado por Balta :)

import socket
import urllib.request
import time
from colorama import init, Fore
import os

os.system("clear")

    loop = tqdm(total=10000, position=0, leave=False)
    for k in range(10000):
        loop.set_description(Fore.LIGHTRED_EX + 'Opening Script'.format(k))
        loop.update(1)
    loop.close()
    
while True:
    print(Fore.YELLOW + """
 _  ____        ____  ____ 
/ \/  __\      /  __\/  __\ ->Balta
| ||  \/|_____ |  \/||  \/|
| ||  __/\____\|  __/|  __/
\_/\_/         \_/   \_/   """)
    print(Fore.YELLOW + "1", end="")
    print(Fore.GREEN + ") ", end="")
    print(Fore.BLUE + "C", end="")
    print(Fore.RED + "a", end="")
    print(Fore.CYAN + "p", end="")
    print(Fore.MAGENTA + "t", end="")
    print(Fore.WHITE + "u", end="")
    print(Fore.YELLOW + "r", end="")
    print(Fore.RED + "a", end="")
    print(Fore.YELLOW + "r ", end="")
    print(Fore.GREEN + "m", end="")
    print(Fore.BLUE + "i ", end="")
    print(Fore.YELLOW + "I", end="")
    print(Fore.GREEN + "P")
    print(Fore.YELLOW + "2", end="")
    print(Fore.GREEN + ") ", end="")
    print(Fore.BLUE + "C", end="")
    print(Fore.RED + "a", end="")
    print(Fore.CYAN + "p", end="")
    print(Fore.MAGENTA + "t", end="")
    print(Fore.WHITE + "u", end="")
    print(Fore.YELLOW + "r", end="")
    print(Fore.RED + "a", end="")
    print(Fore.YELLOW + "r ", end="")
    print(Fore.GREEN + "m", end="")
    print(Fore.BLUE + "i ", end="")
    print(Fore.YELLOW + "I", end="")
    print(Fore.GREEN + "P ", end="")
    print(Fore.CYAN + "E", end="")
    print(Fore.MAGENTA + "x", end="")
    print(Fore.WHITE + "t", end="")
    print(Fore.YELLOW + "e", end="")
    print(Fore.RED + "r", end="")
    print(Fore.YELLOW + "n", end="")
    print(Fore.YELLOW + "a",)
    print(Fore.GREEN + "3", end="")
    print(Fore.BLUE + ") ", end="")
    print(Fore.MAGENTA + "C", end="")
    print(Fore.WHITE + "a", end="")
    print(Fore.YELLOW + "p", end="")
    print(Fore.RED + "t", end="")
    print(Fore.YELLOW + "u", end="")
    print(Fore.YELLOW + "r", end="")
    print(Fore.GREEN + "a", end="")
    print(Fore.BLUE + "r ", end="")
    print(Fore.RED + "I", end="")
    print(Fore.CYAN + "P ", end="")
    print(Fore.MAGENTA + "d", end="")
    print(Fore.WHITE + "e ", end="")
    print(Fore.YELLOW + "u", end="")
    print(Fore.RED + "n ", end="")
    print(Fore.YELLOW + "S", end="")
    print(Fore.GREEN + "e", end="")
    print(Fore.BLUE + "r", end="")
    print(Fore.YELLOW + "v", end="")
    print(Fore.GREEN + "i", end="")
    print(Fore.YELLOW + "d", end="")
    print(Fore.GREEN + "o", end="")
    print(Fore.BLUE + "r ", end="")
    print(Fore.RED + "W", end="")
    print(Fore.CYAN + "e", end="")
    print(Fore.MAGENTA + "b")
    print(Fore.WHITE + "4", end="")
    print(Fore.YELLOW + ") ", end="")
    print(Fore.RED + "S", end="")
    print(Fore.YELLOW + "a", end="")
    print(Fore.GREEN + "l", end="")
    print(Fore.BLUE + "i", end="")
    print(Fore.YELLOW + "r", end="")
    print()

    Elegir = int(input(">>> Seleccione: "))

    if Elegir == 1:
        hostname = socket.gethostname()
        ip_address1 = socket.gethostbyname(hostname)
        print(f"\nSu nombre de host es: {hostname}")
        print(f"Su dirección IP interna es: {ip_address1}")

    elif Elegir == 3:
        ip = input("\n>>> Introduzca el Servidor Web: ")
        ip_address2 = socket.getaddrinfo(ip, 80)
        print(f"\nLa dirección IP es: {ip_address2}")

    elif Elegir == 2:
        external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        print("\nSu dirección IP externa es: {} ".format(external_ip))

    elif Elegir == 4:
        exit()

    else:
        print("\nSeleccione una Opción Valida")

    time.sleep(3)
