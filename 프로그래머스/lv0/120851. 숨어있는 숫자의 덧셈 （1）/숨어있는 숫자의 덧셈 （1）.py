def solution(my_string):
    answer = 0
    a = ["1","2","3","4","5","6","7","8","9","10"]
    # 자연수의 합을 return
    for i in my_string:
        if i in a:
            answer += int(i)
    return answer