import numpy as np


def min_max(number_list):
    min_val = np.amin(number_list)
    max_val = np.amax(number_list)
    minmax_out = (min_val, max_val)
    return minmax_out
