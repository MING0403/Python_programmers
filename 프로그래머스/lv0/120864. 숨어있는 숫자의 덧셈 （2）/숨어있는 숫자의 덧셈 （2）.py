def solution(my_string):
    # 결과를 저장할 변수를 초기화
    answer = 0
    
    # 문자열을 순회하면서 숫자를 추출
    num_str = ""
    for char in my_string:
        if char.isdigit():  # 만약 현재 문자가 숫자라면
            num_str += char  # 숫자를 num_str에 추가
        else:
            # 숫자가 아닌 문자를 만나면, 지금까지의 숫자를 합산하고 num_str을 초기화
            if num_str:
                answer += int(num_str)
                num_str = ""
    
    # 마지막 숫자를 처리
    if num_str:
        answer += int(num_str)
    
    return answer