###
# 야근 지수
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/12927
# status : solved
# time : ???? 
###


from heapq import heapify, heappop, heappush

def solution(n, works):
    if sum(works) <= n :
        return 0
    works = [-x for x in works]
    heapify(works)
    cnt = 0
    while cnt < n :
        num = -heappop(works)
        heappush(works, -num+1)
        cnt += 1
    
    return sum([x**2 for x in works])
