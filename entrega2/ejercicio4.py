'''
========================================================================================================================================================================================================================================
                      Ejercicio sort + merge
Enunciado:
  sort + merge (del modo en que se explicó en la clase).
========================================================================================================================================================================================================================================
    Seminario de Programación Paralela y Concurrente. UNSAM (Universidad Nacional de San Martin)
Autora: Mel Oviedo M
Carrera: TPI.
Año: 2025
Fecha límite de entrega: 14/09/2025
========================================================================================================================================================================================================================================
'''
import threading

def ordenar_sublista(sublista, resultado, indice):
    resultado[indice] = sorted(sublista)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

def sort_merge(arr):
    mid = len(arr) // 2
    izquierda = arr[:mid]
    derecha = arr[mid:]

    # Estructura compartida para guardar resultados
    resultado_parcial = [None, None]

    # Creo hilos
    t1 = threading.Thread(target=ordenar_sublista, args=(izquierda, resultado_parcial, 0))
    t2 = threading.Thread(target=ordenar_sublista, args=(derecha, resultado_parcial, 1))

    # Inicializo los hilos
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    # Merge final
    return merge(resultado_parcial[0], resultado_parcial[1])

# Ejemplo de uso
arr = [8, 3, 5, 1, 7, 9, 2, 6, 4]
print("Array original:", arr)
ordenado = sort_merge(arr)
print("Array ordenado:", ordenado)