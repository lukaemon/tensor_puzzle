import numpy as np


def arange(n: int):
    return np.array(range(n))


def where(q, a, b):
    return q * a + ~q * b


tensor = np.array
