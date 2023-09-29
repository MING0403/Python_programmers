def solution(my_string):
    my_string_lst = list(my_string)
    
    answer_lst=[]
    for i in my_string_lst:
        if i.islower() is True:
            answer_lst.append(i.upper())
        else:
            answer_lst.append(i.lower())
    
    answer = ""
    for j in answer_lst:
        answer += "".join(j)
    
    return answer