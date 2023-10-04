def solution(my_string):
    answer = []
    int_lst = ["0","1","2","3","4","5","6","7","8","9","10"]
    for i in my_string:
        if i in int_lst:
            answer.append(int(i))
            answer.sort()
    return answer