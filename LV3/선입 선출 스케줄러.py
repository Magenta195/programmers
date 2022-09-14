###
# 선입 선출 스케줄러
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/12920
# status : solved
# time : 01:04:33
###

def solution(n, cores):
    cores_num = len(cores)
    
    if n <= cores_num :
        return n
    
    n -= cores_num
    start, end = 1, 10000*10000
    min_time = end
    
    while start <= end :
        mid = (start + end) // 2
        cnt = 0
        
        for core in cores :
            cnt += mid // core
            if cnt >= n : 
                break
                
        if cnt >= n :
            min_time = min(min_time, mid)
            end = mid - 1
        else :
            start = mid + 1
    
    for i in range(len(cores)) :
        n -= (min_time-1) // cores[i]
        if n == 0 :
            return i
    for i in range(len(cores)) :
        if min_time % cores[i] == 0 :
            n -= 1
            if n == 0 :
                return i+1
            
    return 0
