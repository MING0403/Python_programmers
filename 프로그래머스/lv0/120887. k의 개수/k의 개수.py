def solution(i, j, k):
    answer_lst = []
    answer = 0
    # 3,4,5,6,7,8,9,10 -> 2등장 0
    # 1,2,3,4,5,6,7,8,9,10,11,12,13 -> 1등장 6
    
    for num in range(i,j+1):
        num = str(num)
        for num_1 in range(len(num)):
            answer_lst.append(num[num_1])
    
    for num_2 in answer_lst:
        if num_2 == str(k):
            answer += 1
    return answer