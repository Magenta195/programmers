###
# 스킬트리
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/49993
# status : solved
# time: 00:12:51
###

def solution(skill, skill_trees):
    alphabet_list = list(map(chr, range(ord('A'), ord('Z')+1)))
    required_skill = {key : key for key in alphabet_list}
    answer = 0
    
    skill_pre = skill[0]
    if len(skill) > 1 :
        for _skill in skill[1:] :
            required_skill[_skill] = skill_pre
            skill_pre = _skill

    for skill_tree in skill_trees :
        flg = True
        visited = {key : False for key in alphabet_list}
        for _skill in skill_tree :
            _required = required_skill[_skill]
            if _skill != _required and not visited[_required] :
                flg = False
                break
            visited[_skill] = True
        if flg : answer += 1

    return answer
