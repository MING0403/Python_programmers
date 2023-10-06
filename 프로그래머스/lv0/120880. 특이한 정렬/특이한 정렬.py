def solution(numlist, n):
    # 절댓값에 대해 내림차순으로 정렬
    answer = sorted(numlist, key = lambda x:(abs(x-n), -x))
    return answer