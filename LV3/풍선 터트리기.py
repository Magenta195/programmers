###
# 풍선 터트리기
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/68646
# status : solved
# time : 00:15:55
###

def solution(a):
    length = len(a)
    if length < 3 :
        return length
    
    left_min = [a[0]]*length
    right_min = [a[-1]]*length
    
    for i in range(1, length):
        left_min[i] = min(left_min[i-1], a[i])
        right_min[length-1-i] = min(right_min[length-i], a[length-1-i])
        
    answer = 2
    for i in range(1, length-1):
        if max(a[i], left_min[i-1], right_min[i+1]) == a[i] :
            continue
        answer += 1
    
    return answer
