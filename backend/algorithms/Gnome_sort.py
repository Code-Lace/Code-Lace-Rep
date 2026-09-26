def gnome_sort(lista):
    arr = lista.copy()
    i = 0
    n = len(arr)
    
    while i < n:
        if i == 0 or arr[i] >= arr[i - 1]:
            i += 1  # Avanza si está en orden
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]  # Intercambia
            i -= 1  # Retrocede un paso
            
    return arr