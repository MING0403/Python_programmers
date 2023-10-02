def solution(sides):
    answer = 0
    sides.sort()
    tri = 0
    for i in range(0,2):
        tri += sides[i]
        
    if max(sides) >= tri:
        answer = 2
    else: answer = 1
    return answer