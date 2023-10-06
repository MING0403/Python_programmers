def solution(hp):
    # 장군개미는 5의 공격력을, 병정개미는 3의 공격력을 일개미는 1의 공격력
    answer = (hp//5) + ((hp%5)//3) + (((hp%5)%3)//1)
    
    return answer