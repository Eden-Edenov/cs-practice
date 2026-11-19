import numpy as np


def make_hours() -> list[int]:
    return np.arange(0, 24, 3, dtype=int).tolist()