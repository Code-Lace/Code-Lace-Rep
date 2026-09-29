import time

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from algorithms import BubbleSort, Exchange_sort, Gnome_sort, Insertion_sort
from algorithms import MergeSort, QuickSort, SelectionSort, StoogeSort
from algorithms.trace_utils import get_display_source


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


SORTERS = {
    "bubble": (BubbleSort.bubble_sort, BubbleSort),
    "selection": (SelectionSort.selection_sort, SelectionSort),
    "insertion": (Insertion_sort.insertion_sort, Insertion_sort),
    "exchange": (Exchange_sort.exchange_sort, Exchange_sort),
    "gnome": (Gnome_sort.gnome_sort, Gnome_sort),
    "stooge": (StoogeSort.stooge_sort, StoogeSort),
    "merge": (MergeSort.merge_sort, MergeSort),
    "quick": (QuickSort.quick_sort, QuickSort),
}


def sort_data(algo_name, data, on_step=None):
    sort_function, _ = SORTERS[algo_name]
    arr = data.copy()
    result = sort_function(arr, on_step=on_step)
    return arr if result is None else result


@app.post("/api/sort/{algo_name}")
def run_sort(algo_name: str, request: SortRequest):
    if algo_name not in SORTERS:
        return {"error": "Algoritmo no registrado"}

    start = time.perf_counter()
    arr = sort_data(algo_name, request.data)
    duration = (time.perf_counter() - start) * 1000

    return {
        "algorithm": algo_name,
        "sorted_data": arr,
        "time_ms": round(duration, 4)
    }


@app.post("/api/visualize/{algo_name}")
def visualize_sort(algo_name: str, request: SortRequest):
    if algo_name not in SORTERS:
        raise HTTPException(status_code=404, detail="Algoritmo no registrado")

    steps = []
    start = time.perf_counter()
    arr = sort_data(algo_name, request.data, on_step=steps.append)
    duration = (time.perf_counter() - start) * 1000
    _, module = SORTERS[algo_name]
    source, map_source_line = get_display_source(module)
    for step in steps:
        direction = "next" if step["comparing"] else "previous" if step["swapping"] else "last"
        step["line"] = map_source_line(step["line"], direction)

    return {
        "algorithm": algo_name,
        "sorted_data": arr,
        "time_ms": round(duration, 4),
        "steps": steps,
        "source": source,
    }