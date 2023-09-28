def solution(s1, s2):

     # s1과 s2의 교집합
    common_elements = set(s1) & set(s2)
    
    # 교집합의 크기를 반환
    answer = len(common_elements)
    return answer