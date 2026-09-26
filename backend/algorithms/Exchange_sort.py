def exchange_sort(lista):
    """
    Ordenamiento por Intercambio Directo (Exchange Sort).
    Complejidad: O(N^2)
    """
    arr = lista.copy()
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            # Si el elemento posterior es menor, intercambia de inmediato
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr