def merge_sort_simple(arr):
    # 1. Parto el array a la mitad
    mid = len(arr) // 2
    izquierda = arr[:mid]
    derecha = arr[mid:]
    
    # 2. Ordeno cada mitad (acá uso sorted para simplificar
    #    pero se puede implementar el metodo de burbujeo)
    izquierda = sorted(izquierda)
    derecha = sorted(derecha)
    
    # 3. Merge de ambas mitades
    resultado = []
    i = j = 0
    
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    
    # Agrego lo que sobre
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    
    return resultado

# Ejemplo
arr = [8, 3, 5, 1, 7, 9, 2, 6]
print("Array original:", arr)
print("Array ordenado:", merge_sort_simple(arr))