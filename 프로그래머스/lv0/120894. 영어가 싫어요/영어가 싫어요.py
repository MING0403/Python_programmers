def solution(numbers):
    # 문자열을 리스트로 저장
    nums = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    
    for idx, num in enumerate(nums):
        # numbers에서 idx로 변경
        numbers = numbers.replace(num, str(idx))
    
    answer = int(numbers)
        
    return answer