def solution(numbers, direction):
        # 오른쪽으로 회전하는 경우
    if direction == "right":
        # 배열의 마지막 원소를 임시 변수에 저장
        temp = numbers[-1]
        # 배열을 한 칸씩 오른쪽으로 이동
        for i in range(len(numbers) - 1, 0, -1):
            numbers[i] = numbers[i - 1]
        # 임시 변수에 저장한 값을 배열의 첫 번째 원소로 넣어줌
        numbers[0] = temp
    # 왼쪽으로 회전하는 경우
    elif direction == "left":
        # 배열의 첫 번째 원소를 임시 변수에 저장
        temp = numbers[0]
        # 배열을 한 칸씩 왼쪽으로 이동
        for i in range(1, len(numbers)):
            numbers[i - 1] = numbers[i]
        # 임시 변수에 저장한 값을 배열의 마지막 원소로 넣어줌
        numbers[-1] = temp
        
    return numbers