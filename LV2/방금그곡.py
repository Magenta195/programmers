###
# 방금그곡
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/17683
# status : solved
# time : ???
###

replace_dict = { 'C#' : 'H', 'D#' : 'I', 'F#' : 'J', 'G#' : 'K', 'A#' : 'L'}

def replace_sharp(code):
    for key, val in replace_dict.items() :
        code = code.replace(key, val)
    return code

def find_start_and_interval(start, end):
    start_h, start_m = map(int, start.split(':'))
    start_m = start_h*60 + start_m
    end_h, end_m = map(int, end.split(':'))
    end_m = end_h*60 + end_m
    
    return start_m, end_m - start_m

def find_code_infos(start, end, code):
    code_length = len(code)
    start_m, interval = find_start_and_interval(start, end)
    iter_num, left_length = interval // code_length, interval % code_length
    code = iter_num * code + code[:left_length]
    return start_m, interval, code

def solution(m, musicinfos):
    answer = '(None)'
    music_list = []
    m = replace_sharp(m)
    
    for musicinfo in musicinfos :
        start, end, title, code = musicinfo.split(',')
        code = replace_sharp(code)
        start_m, interval, code = find_code_infos(start, end, code)
        
        music_list.append((interval, start_m, title, code))
    
    music_list.sort(key=lambda x : (-x[0], x[1]))

    for _, _, title, code in music_list :
        if m in code :
            answer = title
            break
        
    return answer
