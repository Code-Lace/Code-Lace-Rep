def stooge_sort_rec(arr, l, h):
    """Función recursiva auxiliar para Stooge Sort."""
    if l >= h:
        return

    # Si el primer elemento es mayor que el último, intercambiar
    if arr[l] > arr[h]:
        arr[l], arr[h] = arr[h], arr[l]

    # Si hay 3 o más elementos en el rango
    if h - l + 1 > 2:
        t = (h - l + 1) // 3
        # Aplicar recursivamente a los tercios superpuestos
        stooge_sort_rec(arr, l, h - t)       # Primeros 2/3
        stooge_sort_rec(arr, l + t, h)       # Últimos 2/3
        stooge_sort_rec(arr, l, h - t)       # Primeros 2/3 de nuevo


def stooge_sort(lista):
    """
    Ordenamiento Stooge Sort (Recursivo).
    Complejidad: O(n^(log 3 / log 1.5)) ≈ O(n^2.71)
    """
    arr = lista.copy()
    stooge_sort_rec(arr, 0, len(arr) - 1)
    return arr