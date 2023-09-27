def solution(babbling):
    # "aya", "ye", "woo", "ma"말만 함
    voice = ["aya", "ye", "woo", "ma"]
    # voice에 있는 단어가 있으면 #으로 변경
    rep=[]
    for i in babbling:
        for j in voice:
            i = i.replace(j,"#")
        rep.append(i)
    # #으로만 구성되어 있으면 발음 가능
    answer = 0
    for i in rep:
        i = set(i)
        if len(i)==1 and '#' in i:
            answer += 1
    return answer