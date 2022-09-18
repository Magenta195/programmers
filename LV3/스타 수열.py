###
# 스타 수열
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/70130
# status : solved
# time : ??
###

from collections import Counter

def solution(a):
    answer = -1
    element_counter = Counter(a)
    
    for key in element_counter.keys() :
        if element_counter[key] <= answer :
            continue
            
        cnt = 0
        idx = 0
        while idx < len(a)-1 :
            if ( a[idx] != key and a[idx+1] != key ) or a[idx] == a[idx+1] :
                idx += 1
                continue
            
            cnt += 1
            idx += 2
        answer = max(answer, cnt)
    
    return answer*2
