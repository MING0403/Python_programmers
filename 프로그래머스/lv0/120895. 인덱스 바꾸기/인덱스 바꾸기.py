def solution(my_string, num1, num2):
    my_string_lst = list(my_string)
    
    my_string_lst[num1], my_string_lst[num2] = my_string_lst[num2], my_string_lst[num1]
    
    answer = "".join(my_string_lst)
    return answer