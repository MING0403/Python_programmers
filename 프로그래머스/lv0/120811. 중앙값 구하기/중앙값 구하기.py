import numpy as np
def solution(array):
    array.sort()
    answer = np.median(array)
    return answer