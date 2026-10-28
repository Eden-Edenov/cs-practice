import numpy as np

def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if not values or width <= 0 or len(values) % width != 0:
        return []

    arr = np.asarray(values, dtype=float).reshape(-1, width)
    return arr.tolist()
