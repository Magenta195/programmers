###
# 금과 은 운반하기
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/86053
# status : solved
# time : 01:32:00
###

def solution(a, b, g, s, w, t):
    if a == b == 0 :
        return 0
    
    start, end = 0, 10**15
    answer = float('inf')
    
    
    while start <= end :
        mid = (start + end) // 2
        total_w = 0
        total_moved_g = 0
        s_list = list()
        left_w_list = list()
        moved_w_list = list()
        for _g, _s, _w, _t in zip(g, s, w, t) :
            if mid < _t : 
                continue
            moved_w = min(_g + _s, (mid + _t) // (2 * _t) * _w)
            moved_g = min(moved_w, _g)
            left_w_list.append(moved_w - moved_g)
            s_list.append(_s)
            moved_w_list.append(moved_w)
            
            total_moved_g += moved_g
            total_w += moved_w
            
        if total_moved_g == 0 or total_w < a + b or total_moved_g < a :
            start = mid + 1
            continue
            
        surplus_w = total_moved_g - a
        total_moved_s = 0
        for _s, _mw, _lw in zip(s_list, moved_w_list, left_w_list) :
            _s = min(_s, _mw)
            if _lw >= _s :
                total_moved_s += _s
            elif _s < _lw + surplus_w :
                total_moved_s += _s
                surplus_w += _lw - _s
            else :
                total_moved_s += _lw + surplus_w
            
        if total_moved_s < b :
            start = mid + 1
            continue
        else :
            answer = min(answer, mid)
            end = mid - 1
        
    return answer
