def solution(array):
    answer = []
    for idx, num in enumerate(array):
        if max(array) == num:
            answer.append(num)
            answer.append(idx)
    return answer