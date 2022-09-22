###
# n진수 구하기
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/17687
# status : solved
# time : 00:22:05
###

str_dict = { key : hex(key)[2].upper() for key in range(16)}

def cal_base(n, num):
    result = ''
    while num > 0 :
        result += str_dict[num % n]
        num //= n
    if result == '' :
        return '0'
    return result

def solution(n, t, m, p):
    answer = ''
    cnt = 0
    cnt_num = 0
    total_len = 0 
    order = p
    while cnt < t :
        result = cal_base(n, cnt_num)
        total_len += len(result)
        if total_len >= order :
            idx = total_len - order
            answer += result[idx]
            order += m
            cnt += 1
        cnt_num += 1
            
    return answer
