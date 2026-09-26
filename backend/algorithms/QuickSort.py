def quick_sort(lista):
	"""Ordena una lista usando Quick Sort."""
	_quick_sort(lista, 0, len(lista) - 1)


def _quick_sort(lista, inicio, fin):
	if inicio >= fin:
		return

	pivote = lista[fin]
	indice_menor = inicio
	for indice in range(inicio, fin):
		if lista[indice] <= pivote:
			lista[indice_menor], lista[indice] = lista[indice], lista[indice_menor]
			indice_menor += 1

	lista[indice_menor], lista[fin] = lista[fin], lista[indice_menor]
	_quick_sort(lista, inicio, indice_menor - 1)
	_quick_sort(lista, indice_menor + 1, fin)
