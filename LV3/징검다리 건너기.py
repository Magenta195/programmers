###
# 징검다리 건너기
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/64062
# status : solved
# time : 00:18:21
###

def solution(stones, k):
    start = 0
    end = max(stones)
    answer = 0
    while start <= end :
        mid = (start + end) // 2
        flg = True
        cnt = 0
        for stone in stones :
            if stone - mid <= 0 :
                cnt += 1
            else :
                cnt = 0
            if cnt >= k :
                flg = False
                break
        if flg :
            answer = max(answer, mid)
            start = mid + 1
        else :
            end = mid - 1
        
    return answer + 1
