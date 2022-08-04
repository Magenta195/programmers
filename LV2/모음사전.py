###
# 모음사전.py
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/84512
# status : solved
# time : 00:08:02
###

def solution(word):
    global cnt
    cnt = 0
    
    def dfs(code, length):
        global cnt
        if code == word :
            return True
        if length == 5 :
            return False
        for alphabet in ['A', 'E', 'I', 'O', 'U'] :
            cnt += 1
            flg = dfs(code+alphabet, length+1)
            if flg : return True
        return False
        
    dfs('',0)
    return cnt
