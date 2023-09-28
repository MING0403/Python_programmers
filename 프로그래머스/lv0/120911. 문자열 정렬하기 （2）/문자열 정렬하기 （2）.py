def solution(my_string):
    answer = ''
    # 소문자, 문자열 정렬
    lower_string = sorted(my_string.lower())
    
    # 리스트를 문자열로 출력
    for i in range(len(lower_string)):
        answer += lower_string[i]

    return answer