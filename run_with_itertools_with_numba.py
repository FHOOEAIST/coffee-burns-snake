import pickle
import timeit
from itertools import product

import cv2 as cv
import numba
import numpy as np
from numba.typed import List as nList
from scipy import ndimage


def fix_array_or_list(matrix):
    if isinstance(matrix, np.ndarray):
        return matrix

    if not matrix:
        raise ValueError("List must contain at least one element")

    new_list = nList()
    for r in matrix:
        new_list.append(r)
    return new_list


def run_with_itertools_with_numba(matrix: list, h: int, w: int, kernel: int = 3):
    filter_pos = fix_array_or_list(list(product(range(kernel), repeat=2)))
    image_pos = fix_array_or_list(product(range(h), range(w)))

    return _run_with_itertools_with_numba(matrix, h, w, filter_pos, image_pos, kernel)

def run_timed(func, matrix: list, h: int, w: int, warmpup:int = 100, measurement:int = 1000, kernel: int = 3):
    # warmup
    warm_up_times = timeit.repeat(lambda: func(matrix, h, w, kernel), number=1, repeat=warmpup)
    run_times = timeit.repeat(lambda: func(matrix, h, w, kernel), number=1, repeat=measurement)
    print(f"WarmUp: {warm_up_times}")
    for x in run_times:
        print(str(x*1000))

if __name__ == '__main__':
    width = 1920  # 20  # 1920
    height = 1080  # 20  # 1080
    kernel_size = 5
    arr = list(np.zeros((height, width)).tolist())
    v = 0
    for r in range(0, height):
        for c in range(0, width):
            arr[r][c] = v
            v += 1
            v %= 255
    n_arr = fix_array_or_list(arr)
    np_arr = np.asarray(arr)
    np_uint_arr = np.asarray(np_arr, dtype=np.uint8)


    run_timed(run_with_itertools_with_numba, n_arr, height, width, 100, 1000, kernel_size)