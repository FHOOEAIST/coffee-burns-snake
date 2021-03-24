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


def run_pure_simple_python_while(matrix: list, h: int, w: int, kernel: int = 3):
    kernel_half = kernel // 2
    # create result array
    res = [[0 for _ in range(w)] for _ in range(h)]
    # iterate over height/rows
    r = 0
    while r < h:
        c = 0
        while c < w:
            # prepare result calculation
            sums = 0
            cnt = 0
            r_offset = 0
            # iterate kernel size height/rows
            while r_offset < kernel:
                c_offset = 0
                # iterate kernel size width/col
                while c_offset < kernel:
                    # calc final position
                    pos_r = r + r_offset - kernel_half
                    pos_c = c + c_offset - kernel_half
                    # check if position is valid
                    if 0 <= pos_r < h and 0 <= pos_c < w:
                        # sum up values
                        sums += matrix[pos_r][pos_c]
                        cnt += 1
                    c_offset += 1
                r_offset += 1
            # calculate final result for position
            res[r][c] = sums // cnt
            c += 1
        r += 1
    return res


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

    run_timed(run_pure_simple_python_while, arr, height, width, 25, 100, kernel_size)

