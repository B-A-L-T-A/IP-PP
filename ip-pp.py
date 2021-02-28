#Programado por Balta :)

import socket
import urllib.request
import time
RED = '\033[31m'
WHITE = '\033[37m'

while True:
    print(RED+"""
 _  ____        ____  ____ 
/ \/  __\      /  __\/  __\ ->Balta
| ||  \/|_____ |  \/||  \/|
| ||  __/\____\|  __/|  __/
\_/\_/         \_/   \_/   """)

    print(WHITE+"""
1) Capturar mi IP
2) Capturar mi IP Externa
3) Capturar IP de un Servidor Web 
4) Salir
    """)

    Elegir = int(input(RED+"-> Seleccione: "))

    if Elegir == 1:
        hostname = socket.gethostname()
        ip_address1 = socket.gethostbyname(hostname)
        print(WHITE+f"\nSu nombre de host es: {hostname}")
        print(f"Su dirección IP interna es: {ip_address1}")

    elif Elegir == 3:
        ip = input(RED+"\n-> Introduzca el Servidor Web: ")
        ip_address2 = socket.getaddrinfo(ip, 80)
        print(WHITE+f"\nLa dirección IP es: {ip_address2}")

    elif Elegir == 2:
        external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        print(WHITE+"\nSu dirección IP externa es: {} ".format(external_ip))

    elif Elegir == 4:
        exit()

    else:
        print("\nSeleccione una Opción Valida")

    time.sleep(3)