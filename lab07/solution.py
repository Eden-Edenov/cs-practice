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

def column_means(matrix: list[list[float]]) -> list[float]:
    if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
        return []

    arr = np.asarray(matrix, dtype=float)
    means = np.mean(arr, axis=0)
    means_rounded = np.round(means, 6)
    return means_rounded.tolist()

def column_range(matrix: list[list[float]], column: int) -> float:
    if not matrix or len(matrix) == 0 or column >= len(matrix[0]):
        return 0.0

    arr = np.asarray(matrix, dtype=float)
    col_data = arr[:, column]
    col_min = np.min(col_data)
    col_max = np.max(col_data)

    span = col_max - col_min
    return float(np.round(span, 6))