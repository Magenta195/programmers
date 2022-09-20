###
# 다음 큰 수
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/12911
# status : solved
# time : 00:03:11
###

def solution(n):
    num = n + 1
    cnt = bin(n).count('1')
    
    while True:
        if bin(num).count('1') == cnt :
            return num
        num += 1
    return -1
