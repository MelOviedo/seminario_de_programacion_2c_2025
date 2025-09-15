'''
========================================================================================================================================================================================================================================
                                        Ejercicio Primer intento de exclusión mutua
Enunciado:
  Escribir en pseudocódigo el primer intento de solución de exclusión mutua (que usa turnos) para N
  procesos. Opcionalmente, implementarlo en Python.
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
from colorama import Fore, Style, init

init()  # Inicializa colorama 
# Colores para diferenciar cada proceso
colores = [Fore.GREEN, 
           Fore.YELLOW, 
           Fore.BLUE, 
           Fore.MAGENTA, 
           Fore.CYAN, 
           Fore.RED]

# Variable compartida que indica a quién le toca
turno = 0

# Lock para evitar que se impriman cosas mezcladas
imprimir_lock = threading.Lock()

def proceso(i,N):
    global turno
    while True:
        while turno != i:
          time.sleep(0.5)  # Evita consumir 100% CPU en espera activa

        # ....:Sección crítica:.....
        color= colores[i % len(colores)]
        estilo=Style.BRIGHT
        with imprimir_lock:
            print(color + estilo + f"Proceso {i}"+ Style.RESET_ALL)
            print(color + estilo + f"\tEntrando a sección crítica"+ Style.RESET_ALL)
        time.sleep(1)  # Simula trabajo dentro de la sección crítica

        with imprimir_lock:
            print(color + estilo + f"\tSaliendo de sección crítica"+ Style.RESET_ALL)

        # Pasa el turno al siguiente proceso
        turno = (i + 1) % N

        # ....:Sección no crítica:....
        time.sleep(1)  # Simula que hace otras tareas


def main():
    # Número de procesos 
    #N = 3
    N=int(input("Ingrese cantidad de procesos:"))

    # Creo e inicio los hilos (cada uno representa un proceso)
    for i in range(N):
        threading.Thread(target=proceso, args=(i,N), daemon=True).start()

    # Tiempo de ejercución del programa
    time.sleep(15)

if __name__ == "__main__":
    main()