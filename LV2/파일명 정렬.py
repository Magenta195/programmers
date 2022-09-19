###
# 파일명 정렬
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/17686
# status : solved
# time : 00:25:07
###

import re

def solution(files):
    answer = []
    for idx, file in enumerate(files) :
        matchobj = re.match('([^0-9]*)([0-9]*)(.*)', file)
        head = matchobj.group(1)
        number = matchobj.group(2)
        tail = matchobj.group(3)
        answer.append([head, number, tail, idx])

    answer.sort(key = lambda x : (x[0].upper(), int(x[1]), x[3]))
    answer = [ x[0]+x[1]+x[2] for x in answer]
    
    return answer
