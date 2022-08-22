###
# 양궁대회
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/92342
# status : solved
# time : 00:33:05
###

def solution(n, info):
    global max_score_gap, max_ryan_info
    max_score_gap = -float('inf')
    max_ryan_info = [-1]
    ryan_info = [0]*11
    
    def dfs(left_arrow, gap, pos, ryan_info):
        global max_score_gap, max_ryan_info
        if pos > 10 :
            if gap <= 0 or gap < max_score_gap :
                return
            flg = False
            if left_arrow > 0 :
                ryan_info[-1] += left_arrow
            if gap == max_score_gap :
                for i in range(10, -1, -1):
                    if ryan_info[i] > max_ryan_info[i] :
                        flg = True
                        break
                    elif ryan_info[i] < max_ryan_info[i] : 
                        break
            if gap > max_score_gap or flg :
                max_score_gap = gap
                max_ryan_info = ryan_info
            return
        
        apeach_hit = info[pos]
        if left_arrow > apeach_hit :
            next_ryan_info = ryan_info[:]
            next_ryan_info[pos] += apeach_hit + 1
            dfs(left_arrow - apeach_hit - 1, gap+10-pos, pos+1, next_ryan_info)
        
        next_gap = gap if apeach_hit == 0 else gap-10+pos
        dfs(left_arrow, next_gap, pos+1, ryan_info)
    
    dfs(n,0,0,ryan_info)
    return max_ryan_info
