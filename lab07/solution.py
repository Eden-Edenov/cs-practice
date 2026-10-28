import numpy as np

def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if not values or width <= 0 or len(values) % width != 0:
        return []

    arr = np.asarray(values, dtype=float).reshape(-1, width)
    return arr.tolist()

def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    if not matrix or not rows or not columns:
        return []

    arr = np.asarray(matrix, dtype=float)
    sub_block = arr[np.ix_(rows, columns)]
    return sub_block.tolist()