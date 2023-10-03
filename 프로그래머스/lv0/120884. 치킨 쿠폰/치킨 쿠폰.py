def solution(chicken):
    # answer = -1
    answer = 0
    while chicken >= 10:
        div, mod = divmod(chicken, 10)
        answer += div
        chicken = div+mod
    return answer