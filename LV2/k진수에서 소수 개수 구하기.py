###
# k진수에서 소수 개수 구하기
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/92335
# status : solved
# time : 00:20:42
###

def solution(n, k):
    num = ''
    while n :
        num = str(n%k) + num
        n //= k
    if num == '' : num = '0'
    num_list = list(num.split('0'))
    prime = 0
    
    for _num in num_list :
        if _num == '' or _num == '1':
            continue
        for j in range(2, int(int(_num)**0.5) + 1) :
            if int(_num) % j == 0:
                break
        else :
            prime += 1
    
    return prime
