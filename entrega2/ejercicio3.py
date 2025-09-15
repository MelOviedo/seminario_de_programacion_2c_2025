'''
========================================================================================================================================================================================================================================
                      Ejercicio Bakery de 3 procesos
Enunciado:
  Implementar una versión de Bakery para 3 procesos, lo más simple que se pueda.
========================================================================================================================================================================================================================================
    Seminario de Programación Paralela y Concurrente. UNSAM (Universidad Nacional de San Martin)
Autora: Mel Oviedo M
Carrera: TPI.
Año: 2025
Fecha límite de entrega: 14/09/2025
========================================================================================================================================================================================================================================
'''
import threading
import time
from colorama import Fore, Back, Style, init

init()

# Números asignados para cada proceso (0 = no quiere entrar)
numeros = [0, 0, 0] #[P, Q, R]

lock = threading.Lock()

intentos = 5

def tomar_numero(i):
    #Proceso i toma un número mayor al máximo actual
    with lock:
        numeros[i] = max(numeros) + 1
        mi_num = numeros[i]
    return mi_num

def liberar_numero(i):
    #Proceso i libera su número->vuelve a 0
    with lock:
        numeros[i] = 0

def proceso(i, color, nombre):
    for _ in range(intentos):
        mi_num = tomar_numero(i)
        print(Fore.BLACK + color + Style.BRIGHT + f"{nombre} ---> Entra a la sección crítica con número {mi_num} (estado: {numeros})" + Style.RESET_ALL)

        #tiempo en la sección crítica
        time.sleep(0.5)

        print(Fore.BLACK + color + Style.BRIGHT + f"{nombre} ---> Sale de la sección crítica con número {mi_num} (estado: {numeros})" + Style.RESET_ALL)
        
        #resetea su número
        liberar_numero(i)

        time.sleep(0.2)

# Creo hilos para 3 procesos
hilo_p = threading.Thread(target=proceso, args=(0, Back.WHITE, "Proceso P"))
hilo_q = threading.Thread(target=proceso, args=(1, Back.BLUE, "Proceso Q"))
hilo_r = threading.Thread(target=proceso, args=(2, Back.RED, "Proceso R"))

# Inicio hilos
hilo_p.start()
hilo_q.start()
hilo_r.start()

hilo_p.join()
hilo_q.join()
hilo_r.join()
