###
# 점프와 순간 이동
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/12980
# status : solved
# time : 00:27:15
###

def solution(n):
    ans = 1
    while n > 1 :
        if n % 2 == 1 :
            ans += 1
        n //= 2

    return ans
