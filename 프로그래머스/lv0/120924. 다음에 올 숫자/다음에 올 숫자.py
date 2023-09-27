def solution(common):
    # 등차수열인지, 등비수열인지 판단
    # 등차수열이라면
    if common[1] - common[0] == common[-1] - common[-2]:
        next_num = common[-1] + (common[1] - common[0])
    # 등비수열인 경우
    else:
        next_num = common[-1] * (common[1] // common[0])
    return next_num