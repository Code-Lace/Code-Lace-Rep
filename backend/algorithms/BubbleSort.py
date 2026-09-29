from algorithms.trace_utils import record_step


def bubble_sort(lista, on_step=None):
	"""Ordena una lista usando Bubble Sort"""
	n = len(lista)
	sorted_indices = []
	for i in range(n):
		for j in range(0, n - i - 1):
			record_step(on_step, lista, comparing=[j, j + 1], sorted_indices=sorted_indices)
			if lista[j] > lista[j + 1]:
				lista[j], lista[j + 1] = lista[j + 1], lista[j]
				record_step(on_step, lista, swapping=[j, j + 1], sorted_indices=sorted_indices)
		sorted_indices.append(n - i - 1)
	record_step(on_step, lista, sorted_indices=range(n))
