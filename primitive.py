import numpy as np


def arange(n: int):
    return np.array(range(n))


def where(condition, a, b):
    return condition * a + ~condition * b


tensor = np.array
