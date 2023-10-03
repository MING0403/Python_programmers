def solution(bin1, bin2):
    # answer = ''
    bin1_10 = int(bin1, 2)
    bin2_10 = int(bin2, 2)
    answer = bin(bin1_10 + bin2_10)
    return answer[2:]