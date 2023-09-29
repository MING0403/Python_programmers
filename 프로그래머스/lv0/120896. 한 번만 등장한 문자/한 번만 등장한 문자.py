def solution(s):
    answer_lst = []
    for i in s:
        if s.count(i)==1:
            answer_lst.append(i)
    
    answer = ""
    for j in sorted(answer_lst):
        answer += "".join(j)
    return answer