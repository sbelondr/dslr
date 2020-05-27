import math
import numpy as np

def ft_count(arr):
    cnt = 0
    for x in arr:
        if not math.isnan(x):
            cnt += 1
    return cnt

def ft_mean(arr):
    cnt = 0
    sum_arr = 0
    for x in arr:
        if not math.isnan(x):
            cnt += 1
            sum_arr += x
    sum_arr /= cnt
    final = sum_arr
    return final

def ft_std(arr):
    mean = ft_mean(arr)
    result = (arr - mean)**2
    final = ft_mean(result)
    final = final**(0.5)
    return final

def ft_min(arr):
    min_arr = arr[0]
    for x in arr:
        if x < min_arr:
            min_arr = x
    return min_arr

def ft_max(arr):
    max_arr = arr[0]
    for x in arr:
        if x > max_arr:
            max_arr = x
    return max_arr

def ft_percentile(arr, p):
    new_arr = np.array(arr)
    new_arr.sort()
    size = ft_count(new_arr) - 1
    k = size * (p / 100)
    floor = np.floor(k)
    ceil = np.ceil(k)
    if floor == ceil:
        return new_arr[int(k)]
    d0 = new_arr[int(floor)] * (ceil - k)
    d1 = new_arr[int(ceil)] * (k - floor)
    d = d0 + d1
    return d
