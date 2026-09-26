from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time

# Importamos los algoritmos desde la carpeta algorithms
from algorithms.BubbleSort import bubble_sort
from algorithms.SelectionSort import selection_sort
from algorithms.Insertion_sort import insertion_sort
from algorithms.Exchange_sort import exchange_sort
from algorithms.Gnome_sort import gnome_sort
from algorithms.StoogeSort import stooge_sort
from algorithms.MergeSort import merge_sort
from algorithms.QuickSort import quick_sort


app = FastAPI(title="Code & Lace Backend", version="1.0")

# Permitir conexiones desde el Frontend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SortRequest(BaseModel):
    data: list[int]

@app.post("/api/sort/{algo_name}")
def run_sort(algo_name: str, request: SortRequest):
    arr = request.data.copy()
    start = time.perf_counter()

    if algo_name == "bubble":
        bubble_sort(arr)
    elif algo_name == "selection":
        selection_sort(arr)
    elif algo_name == "insertion":
        insertion_sort(arr)
    elif algo_name == "exchange":
        arr = exchange_sort(arr)
    elif algo_name == "gnome":
        arr = gnome_sort(arr)
    elif algo_name == "stooge":
        arr = stooge_sort(arr)
    elif algo_name == "merge":
        merge_sort(arr)
    elif algo_name == "quick":
        quick_sort(arr)
    else:
        return {"error": "Algoritmo no registrado"}

    duration = (time.perf_counter() - start) * 1000    # Son en Milisegundos

    return {
        "algorithm": algo_name,
        "sorted_data": arr,
        "time_ms": round(duration, 4)
    }