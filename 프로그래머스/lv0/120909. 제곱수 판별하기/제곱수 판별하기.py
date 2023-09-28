import math

def solution(n):
    # n이 음수인 경우 무조건 2를 반환
    if n < 0:
        return 2
    
    # n이 양수인 경우, 제곱근을 계산하고 이를 반올림한 값과 비교
    sqrt_n = math.isqrt(n)
    if sqrt_n * sqrt_n == n:
        return 1
    else:
        return 2