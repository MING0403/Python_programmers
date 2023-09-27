def solution(num, total):

    answer=[]
    # num개의 연속된 정수의 평균 값
    average = total // num
    
    # average - (num-1)//2 : 연속된 정수 중 첫 번째 정수
    # average + (num+2)//2 : num개의 연속된 정수 중 마지막 정수
    for i in range(average - (num-1)//2, average + (num + 2)//2):
        answer.append(i)
        
    return answer