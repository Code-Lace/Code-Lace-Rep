from algorithms.trace_utils import record_step


def stooge_sort_rec(arr, l, h, on_step=None):
    """Función recursiva auxiliar para Stooge Sort."""
    if l >= h:
        return

    record_step(on_step, arr, comparing=[l, h])
    # Si el primer elemento es mayor que el último, intercambiar
    if arr[l] > arr[h]:
        arr[l], arr[h] = arr[h], arr[l]
        record_step(on_step, arr, swapping=[l, h])

    # Si hay 3 o más elementos en el rango
    if h - l + 1 > 2:
        t = (h - l + 1) // 3
        # Aplicar recursivamente a los tercios superpuestos
        stooge_sort_rec(arr, l, h - t, on_step)       # Primeros 2/3
        stooge_sort_rec(arr, l + t, h, on_step)       # Últimos 2/3
        stooge_sort_rec(arr, l, h - t, on_step)       # Primeros 2/3 de nuevo


def stooge_sort(lista, on_step=None):
    """
    Ordenamiento Stooge Sort (Recursivo).
    Complejidad: O(n^(log 3 / log 1.5)) ≈ O(n^2.71)
    """
    arr = lista.copy()
    stooge_sort_rec(arr, 0, len(arr) - 1, on_step)
    record_step(on_step, arr, sorted_indices=range(len(arr)))
    return arr