def solution(score):
    
    # 각 학생의 평균 점수를 계산하여 (평균 점수, 학생 번호) 형태의 리스트를 생성
    average_scores = [(sum(scores) / 2, i) for i, scores in enumerate(score, start=1)]
    
    # 평균 점수를 기준으로 내림차순 정렬
    average_scores.sort(reverse=True)
    
    # 각 학생의 등수를 계산하여 결과 리스트에 저장
    result = [0] * len(score)
    rank = 1
    
    for i in range(len(average_scores)):
        result[average_scores[i][1] - 1] = rank
        if i < len(average_scores) - 1 and average_scores[i][0] != average_scores[i + 1][0]:
            rank = i + 2
    
    return result