###
# 줄 서는 방법
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/12936
# status : solved
# time : 00:07:36
###

def factorial(n) :
    if n == 1 :
        return 1
    else :
        return n * factorial(n-1)

def solution(n, k):
    num_list = list(range(1,n+1))
    k -= 1
    left = n
    total = factorial(n)
    answer = []
    while left > 0 :
        idx = k // (total // left)
        answer.append(num_list[idx])
        
        del num_list[idx]
        k %= total // left
        total //= left
        left -= 1
        
    return answer
