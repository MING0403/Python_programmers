def solution(num, k):
    num_str = str(num)
    
    for i, digit_char in enumerate(num_str, start=1):
        if int(digit_char) == k:
            return i

    return -1