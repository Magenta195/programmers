###
# 최고의 집합
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/12938
# status : solved
# time : 00:12:32
###


def solution(n, s):
    if n > s :
        return [-1]
    result_num, left_num = s // n, s % n
    answer = [result_num]*(n-left_num)
    if left_num > 0 : answer.extend([result_num+1]*left_num)
    
    return answer 
