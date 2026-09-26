def insertion_sort(lista):
    """
    Ordenamiento por Inserción.
    Complejidad: O(N^2)
    """
    arr = lista.copy()
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        # Compara la clave con los elementos anteriores y los desplaza
        while j >= 0 and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave
    return arr