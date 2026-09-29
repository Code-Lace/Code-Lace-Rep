import inspect


def record_step(on_step, values, comparing=(), swapping=(), sorted_indices=()):
    if on_step is None:
        return

    caller = inspect.currentframe().f_back
    on_step({
        "array": list(values),
        "comparing": list(comparing),
        "swapping": list(swapping),
        "sorted": list(sorted_indices),
        "line": caller.f_lineno if caller else 1,
    })