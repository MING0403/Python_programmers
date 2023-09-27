def solution(my_str, n):
    answer = []
    
    # 길이를 n개씩 잘라 배열에 저장
    for i in range(0,len(my_str),n):
        answer.append(my_str[i:i+n])
    
    return answer