def solution(n):
    answer = 0
    num=[]
    for i in range(n+1):
        for j in range(1,i+1):
            if i%j==0:
                num.append(i)
        #  count가 3이상(합성수)이면 합성수의 카운트를 1증가
        if num.count(i) >= 3:
            answer += 1
    return answer