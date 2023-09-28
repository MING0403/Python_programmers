def solution(array):
    answer = 0
    # 7이 등장할 때 마다 answer+1
    for num in array:
        # int를 str로 변경
        answer += str(num).count('7')
    return answer