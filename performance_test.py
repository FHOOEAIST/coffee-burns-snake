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


def run_pure_simple_python(matrix: list, h: int, w: int, kernel: int = 3):
    kernel_half = kernel // 2
    # create result array
    res = [[0 for _ in range(w)] for _ in range(h)]
    # iterate over height/rows
    for r in range(0, h):
        # iterate over width/col
        for c in range(0, w):
            # prepare result calculation
            sums = 0
            cnt = 0
            # iterate kernel size height/rows
            for r_offset in range(0, kernel):
                # iterate kernel size width/col
                for c_offset in range(0, kernel):
                    # calc final position
                    pos_r = r + r_offset - kernel_half
                    pos_c = c + c_offset - kernel_half
                    # check if position is valid
                    if 0 <= pos_r < h and 0 <= pos_c < w:
                        # sum up values
                        sums += matrix[pos_r][pos_c]
                        cnt += 1
            # calculate final result for position
            res[r][c] = sums // cnt
    return res


@numba.jit(nopython=True)
def run_pure_simple_python_with_numba(matrix: list, h: int, w: int, kernel: int = 3):
    kernel_half = kernel // 2
    # create result array
    res = [[0 for _ in range(w)] for _ in range(h)]
    # iterate over height/rows
    for r in range(0, h):
        # iterate over width/col
        for c in range(0, w):
            # prepare result calculation
            sums = 0
            cnt = 0
            # iterate kernel size height/rows
            for r_offset in range(0, kernel):
                # iterate kernel size width/col
                for c_offset in range(0, kernel):
                    # calc final position
                    pos_r = r + r_offset - kernel_half
                    pos_c = c + c_offset - kernel_half
                    # check if position is valid
                    if 0 <= pos_r < h and 0 <= pos_c < w:
                        # sum up values
                        sums = sums + matrix[pos_r][pos_c]
                        cnt = cnt + 1
            # calculate final result for position
            res[r][c] = sums // cnt
    return res


@numba.jit(nopython=True, parallel=True)
def run_pure_simple_python_with_numba_parallel(matrix: list, h: int, w: int, kernel: int = 3):
    kernel_half = kernel // 2
    # create result array
    res = [[0 for _ in range(w)] for _ in range(h)]
    # iterate over height/rows
    for r in numba.prange(h):
        # iterate over width/col
        for c in numba.prange(w):
            # prepare result calculation
            sums = 0
            cnt = 0
            # iterate kernel size height/rows
            for r_offset in range(0, kernel):
                # iterate kernel size width/col
                for c_offset in range(0, kernel):
                    # calc final position
                    pos_r = r + r_offset - kernel_half
                    pos_c = c + c_offset - kernel_half
                    # check if position is valid
                    if 0 <= pos_r < h and 0 <= pos_c < w:
                        # sum up values
                        sums = sums + matrix[pos_r][pos_c]
                        cnt = cnt + 1
            # calculate final result for position
            res[r][c] = sums // cnt

    return res


def run_with_itertools(matrix: list, h: int, w: int, kernel: int = 3):
    res = [[0 for _ in range(w)] for _ in range(h)]
    kernel_half = kernel // 2
    filter_pos = list(product(range(kernel), repeat=2))
    image_pos = product(range(h), range(w))
    for r, c in image_pos:
        sums = 0
        cnt = 0
        for r_offset, c_offset in filter_pos:
            pos_r = r + r_offset - kernel_half
            pos_c = c + c_offset - kernel_half
            # check if position is valid
            if 0 <= pos_r < h and 0 <= pos_c < w:
                # sum up values
                sums = sums + matrix[pos_r][pos_c]
                cnt = cnt + 1
        res[r][c] = sums // cnt
    return res


@numba.jit(nopython=True, parallel=True)
def _run_with_itertools_with_numba(_matrix: list, _h: int, _w: int, f_pos, i_pos, _kernel: int = 3):
    res = [[0 for _ in range(_w)] for _ in range(_h)]
    kernel_half = _kernel // 2
    for r, c in i_pos:
        sums = 0
        cnt = 0
        for r_offset, c_offset in f_pos:
            pos_r = r + r_offset - kernel_half
            pos_c = c + c_offset - kernel_half
            # check if position is valid
            if 0 <= pos_r < _h and 0 <= pos_c < _w:
                # sum up values
                sums += _matrix[pos_r][pos_c]
                cnt += 1
        res[r][c] = sums // cnt
    return res


def run_with_itertools_with_numba(matrix: list, h: int, w: int, kernel: int = 3):
    filter_pos = fix_array_or_list(list(product(range(kernel), repeat=2)))
    image_pos = fix_array_or_list(product(range(h), range(w)))

    return _run_with_itertools_with_numba(matrix, h, w, filter_pos, image_pos, kernel)


def run_with_numpy(matrix: list, h: int, w: int, kernel: int = 3):
    kernel_half = kernel // 2
    h_end = h
    w_end = w
    # create result array
    res = np.zeros((h, w), dtype=int)
    # iterate over height/rows
    for r in range(0, h):
        # iterate over width/col
        for c in range(0, w):
            # prepare result calculation
            r_start = r - kernel_half
            r_end = r + kernel_half + 1
            c_start = c - kernel_half
            c_end = c + kernel_half + 1
            if r_start < 0:
                r_start = 0
            if r_end > h_end:
                r_end = h_end
            if c_start < 0:
                c_start = 0
            if c_end > w_end:
                c_end = w_end

            sub = matrix[r_start:r_end, c_start:c_end]
            res[r, c] = np.sum(sub) // sub.size
    return res


@numba.jit(nopython=True)
def run_with_numpy_with_numba(matrix: list, h: int, w: int, kernel: int = 3):
    kernel_half = kernel // 2
    h_end = h
    w_end = w
    # create result array
    res = np.zeros((h, w), dtype=numba.int64)
    # iterate over height/rows
    for r in range(0, h):
        # iterate over width/col
        for c in range(0, w):
            # prepare result calculation
            r_start = r - kernel_half
            r_end = r + kernel_half + 1
            c_start = c - kernel_half
            c_end = c + kernel_half + 1
            if r_start < 0:
                r_start = 0
            if r_end > h_end:
                r_end = h_end
            if c_start < 0:
                c_start = 0
            if c_end > w_end:
                c_end = w_end

            sub = matrix[r_start:r_end, c_start:c_end]
            res[r, c] = np.sum(sub) // sub.size
    return res


@numba.jit(nopython=True, parallel=True)
def run_with_numpy_with_numba_parallel(matrix: list, h: int, w: int, kernel: int = 3):
    kernel_half = kernel // 2
    h_end = h
    w_end = w
    # create result array
    res = np.zeros((h, w), dtype=numba.int64)
    # iterate over height/rows
    for r in numba.prange(0, h):
        # iterate over width/col
        for c in numba.prange(0, w):
            # prepare result calculation
            r_start = r - kernel_half
            r_end = r + kernel_half + 1
            c_start = c - kernel_half
            c_end = c + kernel_half + 1
            if r_start < 0:
                r_start = 0
            if r_end > h_end:
                r_end = h_end
            if c_start < 0:
                c_start = 0
            if c_end > w_end:
                c_end = w_end

            sub = matrix[r_start:r_end, c_start:c_end]
            res[r, c] = np.sum(sub) // sub.size
    return res


def run_with_numpy_and_scipy(matrix: list, h: int, w: int, kernel: int = 3):
    _matrix = np.asarray(matrix)
    conv = np.ones((kernel, kernel), dtype=int) / (kernel * kernel)
    return ndimage.convolve(_matrix, conv, mode='constant', cval=0)


def run_with_opencv(matrix: list, h: int, w: int, kernel: int = 3):
    conv = np.ones((kernel, kernel), dtype=np.float32) / (kernel * kernel)
    return cv.filter2D(matrix, -1, conv)


runs = [(run_pure_simple_python, 0),  # 0
        (run_with_itertools, 0),  # 1
        (run_pure_simple_python_with_numba, 1),  # 2
        (run_pure_simple_python_with_numba_parallel, 1),  # 3
        (run_with_itertools_with_numba, 1),  # 4
        (run_with_numpy, 2),  # 5
        (run_with_numpy_with_numba, 2),  # 6
        (run_with_numpy_with_numba_parallel, 2),  # 7
        (run_with_numpy_and_scipy, 2),  # 8
        (run_with_opencv, 3)  # 9
        ]


def build_run(run_version: int):
    return runs[run_version]


def run_timed(func, matrix: list, h: int, w: int, kernel: int = 3):
    # warmup
    warm_up_times = timeit.repeat(lambda: func(matrix, h, w, kernel), number=1, repeat=25)
    run_times = timeit.repeat(lambda: func(matrix, h, w, kernel), number=1, repeat=100)
    print(f"WarmUp: {warm_up_times}")
    print(f"RunTimes: {run_times}")


def comp(v1, v2):
    with open(v1, 'rb') as f:
        res_v1 = pickle.load(f)
    with open(v2, 'rb') as f:
        res_v2 = pickle.load(f)

    for r in range(len(res_v1)):
        for c in range(len(res_v1[r])):
            if res_v1[r][c] != res_v2[r][c]:
                print(f"Error @ r={r} c={c}")


if __name__ == '__main__':
    # V1 - classic python
    debug_run = False
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

    if debug_run:
        for i in range(0, len(runs)):
            print(f"Run Timed: {i}")
            run, converted = build_run(i)
            if converted == 3:
                run_timed(run, np_uint_arr, height, width, kernel_size)
            if converted == 2:
                res = run(np_arr, height, width, kernel_size)
            elif converted == 1:
                res = run(n_arr, height, width, kernel_size)
            elif converted == 0:
                res = run(arr, height, width, kernel_size)
            else:
                raise ValueError("Not implemented")

            with open(f'rev_v{i}.pickle', 'wb') as f:
                pickle.dump(res, f)

            comp('rev_v0.pickle', f'rev_v{i}.pickle')

    if not debug_run:
        for i in range(0, len(runs)):
            run, converted = build_run(i)
            print(f"Run: {i} - {run.__name__}")
            if converted == 3:
                run_timed(run, np_uint_arr, height, width, kernel_size)
            elif converted == 2:
                run_timed(run, np_arr, height, width, kernel_size)
            elif converted == 1:
                run_timed(run, n_arr, height, width, kernel_size)
            elif converted == 0:
                run_timed(run, arr, height, width, kernel_size)
            else:
                raise ValueError("Not implemented")
