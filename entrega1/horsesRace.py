'''
========================================================================================================================================================================================================================================
                                        Ejercicio Carrera de Caballos
Enunciado:
  Implementar una "carrera de caballos" usando threads, donde cada "caballo" es un Thread o 
  bien un objeto de una clase que sea sub clase de Thread, y contendrá una posición dada por 
  un número entero. El ciclo de vida de este objeto es incrementar la posición en variados 
  instantes de tiempo, mientras no haya llegado a la meta, la cual es simplemente un entero 
  prefijado. Una vez que un caballo llegue a la meta, se debe informar en pantalla cuál fue 
  el ganador, luego de lo cual los demás caballos no deberán seguir corriendo. Imprimir 
  durante todo el ciclo las posiciones de los caballos, o bien de alguna manera el camino 
  que va recorriendo cada uno (usando símbolos Ascii). El programa podría producir un 
  ganador disitnto cada vez que se corra. Opcionalmente, extender el funcionamiento a un 
  array de n caballos, donde n puede ser un parámetro.

========================================================================================================================================================================================================================================

    Seminario de Programación Paralela y Concurrente. UNSAM (Universidad Nacional de San Martin)
Autora: 
Carrera: TPI.
Año: 2025
Fecha límite de entrega: 19/08/2025

========================================================================================================================================================================================================================================
'''

#...............................:Biblotecas a implementar:..............................
from threading import Thread, Event, Lock
import time     #Para simular avances aleatorios de los caballos.
import random   #Para simular avances aleatorios de los caballos.
from typing import List
import os       # Para limpiar la terminal
 
#..........................:Clase Caballo:..........................
class Caballo(Thread):  #Hereda de la clase Thread
  def __init__(self, nombre: str, eventoGanador: Event, lockGanador: Lock) -> None:
    super().__init__()
    self.nombre = nombre                      #Identificador
    self.distanciaRecorrida = 0               #Distancia recorrida por el caballo   
    self.eventoGanador = eventoGanador        #Indica si hay un ganador
    self.lockGanador = lockGanador            #Evita que varios caballos se declaren ganadores
    self.ganador = False                      #Flag para indicar si es el caballo ganador
    self.distanciaCarrera = distanciaCarrera  # Distancia total de la carrera
  
  def correr(self) -> None:
    while not self.eventoGanador.is_set():      #Mientras no haya un ganador sigue corriendo
      tiempoEspera = random.uniform(0.5, 1) #Simulación de velocidad de carrera a tiempo distintos
      time.sleep(tiempoEspera)

      # Antes de avanzar, compruebo si ya hay ganador
      if self.eventoGanador.is_set():
        break

      self.distanciaRecorrida += 1           #Avanza un paso
        
      with printLock: 
        printPositions()        #Imprime posiciones de todos los caballos sin que los hilos se mezclen.

      if self.llegaALaMeta():  #Si llega a la meta
        with self.lockGanador:
          if not self.eventoGanador.is_set():
            self.ganador = True
            self.eventoGanador.set()
        break  # Sale del ciclo inmediatamente después de declarar ganador
    
  def llegaALaMeta(self) -> bool:
    return self.distanciaRecorrida == self.distanciaCarrera

  def run(self):
    self.correr()


#..........................:Funciones utilizadas en el código:..........................
def printPositions():     #Imprime las posiciones de los caballos en el transcurso de la carrera.
  limpiarPantalla()  # Limpia la pantalla antes de imprimir las posiciones

  print(f"Carrera de {len(caballos)} caballos por {distanciaCarrera} metros:\n")  # Titulo de la carrera

  colorGanador= "\033[33m"  # Amarillo
  reset= "\033[0m"          # Color por defecto
  verde = "\033[92m"

  for caballo in caballos:
    color = colorGanador if caballo.ganador else reset
    recorrido = "." * caballo.distanciaRecorrida
    ganador = " \U0001F947" if caballo.ganador else ""
    print(f"{color}{caballo.nombre:<12} {recorrido} \U0001F3C7{ganador}{reset}")

  # --- Línea de meta ---
  #print(f"\n{verde}{'═' * (distanciaCarrera + 10)} \U0001F3C1 Línea de meta{reset}")
  print(f"\n{verde}{'Distancia:':<13}{'═' * distanciaCarrera} \U0001F3C1 Línea de meta{reset}")
  #print("\n" + "═" * (distanciaCarrera + 10)+"<- Línea de meta")

def limpiarPantalla():    # Limpiar pantalla
  os.system('cls' if os.name == 'nt' else 'clear')  

#..................................:Inicio del código:..................................
if __name__ == "__main__":
  global distanciaCarrera, caballos, printLock
  
  #Validación de entrada del usuario
  while True:
    try:
      cantidadDeCaballos = int(input("Cantidad de caballos: "))
      if cantidadDeCaballos <= 0:
        print("Debe ingresar un número mayor que 0.")
      else:
          break
    except ValueError:
      print("Debe ingresar un número entero válido.")

  while True:
    try:
      distanciaCarrera = int(input("Distancia de la carrera: "))
      if distanciaCarrera <= 0:
        print("Debe ingresar un número mayor que 0.")
      else:
        break
    except ValueError:
      print("Debe ingresar un número entero válido.")

  eventoGanador = Event()
  lockGanador = Lock()  # Lock para garantizar que solo un hilo pueda declarar su victoria a la vez
  printLock = Lock()

  # Creo a los caballos
  caballos: List[Caballo] = [Caballo(f"Caballo {i + 1}", eventoGanador, lockGanador) for i in range(cantidadDeCaballos)]

  for caballo in caballos:
    caballo.start()

  for caballo in caballos:
    caballo.join()

  print("Carrera terminada.")
    
  # Mostrar resultados
  print("\nResultados:")
  caballoGanador: Caballo = next((caballo for caballo in caballos if caballo.ganador), None)
  
  if caballoGanador:
    print(f"1° lugar: {caballoGanador.nombre} ¡GANADOR! \U0001F947")

  caballosOrdenados: List[Caballo] = sorted(caballos, key=lambda caballo: caballo.distanciaRecorrida, reverse=True)
  
  i = 1
  for caballo in caballosOrdenados:
    if not caballo.ganador:
      i += 1
      print(f"{i}° lugar: {caballo.nombre}")