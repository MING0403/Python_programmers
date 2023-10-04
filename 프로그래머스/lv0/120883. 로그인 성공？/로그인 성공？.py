def solution(id_pw, db):
    answer_lst = []
    
    for i in db:
        if i == id_pw:
            answer_lst.append(1)
        
        for j in i:
            if id_pw[0] == j:
                answer_lst.append(0)
            else:
                answer_lst.append(2)

    if 1 in answer_lst:
        answer = 'login'
    elif 0 in answer_lst:
        answer='wrong pw'
    elif 2 in answer_lst:
        answer='fail'
    return answer