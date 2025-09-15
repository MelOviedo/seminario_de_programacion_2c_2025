'''
========================================================================================================================================================================================================================================
                      Ejercicio Bakery de 2 procesos
Enunciado:
  Para Bakery de 2 procesos p y q, describir un escenario en que las variables np y nq crecen 
  ilimitadamente.
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

init()  # Inicializa colorama 

np_num = 0
nq_num = 0

lock = threading.Lock()

# Número de veces que cada proceso intentará entrar
intentos = 5

def proceso_p():
    global np_num, nq_num
    for i in range(intentos):
        with lock:
            # P toma un número: máximo actual + 1
            np_num = max(np_num, nq_num) + 1
            mi_num = np_num  # Guarda número asignado
        color= Back.GREEN
        estilo=Style.BRIGHT
        print(Fore.BLACK + color + estilo + f"Proceso P ---> Entra a la sección crítica con número {mi_num}"+ Style.RESET_ALL)
        # tiempo en sección crítica
        time.sleep(0.5)
        print(Fore.BLACK + color + estilo + f"Proceso P ---> Sale de la sección crítica con número {mi_num}"+ Style.RESET_ALL)
        time.sleep(0.2)  # Tiempo antes de intentar nuevamente

def proceso_q():
    global np_num, nq_num
    for i in range(intentos):
        with lock:
            # Q toma un número: máximo actual + 1
            nq_num = max(np_num, nq_num) + 1
            mi_num = nq_num  # Guarda número asignado
        color= Back.CYAN
        estilo=Style.BRIGHT
        print(Fore.BLACK + color + estilo + f"Proceso Q ---> Entra a la sección crítica con número {mi_num}"+ Style.RESET_ALL)
        # tiempo en sección crítica
        time.sleep(0.5)
        print(Fore.BLACK + color + estilo + f"Proceso Q ---> Sale de la sección crítica con número {mi_num}"+ Style.RESET_ALL)
        time.sleep(0.2)  # Tiempo antes de intentar nuevamente

# Creo e inicio los hilos
hilo_p = threading.Thread(target=proceso_p)
hilo_q = threading.Thread(target=proceso_q)

hilo_p.start()
hilo_q.start()


hilo_p.join()
hilo_q.join()