from algorithms.trace_utils import record_step


def merge_sort(arr, on_step=None):
    _merge_sort(arr, on_step, 0, arr)


def _merge_sort(arr, on_step, offset, visual_values):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    _merge_sort(left_half, on_step, offset, visual_values)
    _merge_sort(right_half, on_step, offset + mid, visual_values)

    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
        record_step(on_step, visual_values, comparing=[offset + i, offset + mid + j])
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            visual_values[offset + k] = arr[k]
            record_step(on_step, visual_values, swapping=[offset + k])
            i += 1
        else:
            arr[k] = right_half[j]
            visual_values[offset + k] = arr[k]
            record_step(on_step, visual_values, swapping=[offset + k])
            j += 1
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        visual_values[offset + k] = arr[k]
        record_step(on_step, visual_values, swapping=[offset + k])
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        visual_values[offset + k] = arr[k]
        record_step(on_step, visual_values, swapping=[offset + k])
        j += 1
        k += 1

    if offset == 0:
        record_step(on_step, visual_values, sorted_indices=range(len(arr)))


