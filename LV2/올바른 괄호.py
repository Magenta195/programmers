###
# 올바른 괄호
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/12909
# status : solved
# time : 00:01:58
###

def solution(s):
    stk = []
    for _s in s :
        if _s == ')':
            if not stk : return False
            stk.pop()
        else :
            stk.append(_s)
    return not stk
