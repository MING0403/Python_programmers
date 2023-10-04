def solution(numbers):
    numbers.sort()
    # 두 개를 곱해 만들 수 있는 최댓값
    answer = max(numbers[0]*numbers[1],numbers[-1]*numbers[-2])
    return answer