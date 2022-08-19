###
# 성격 유형 검사하기
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/118666
# status : solved
# time : 00:04:21
###

def solution(survey, choices):
    personality_list = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    personality_dict = { key : 0 for key in personality_list }
    
    for question, choice in zip(survey, choices):
        first_q, second_q = question[0], question[1]
        if choice < 4 :
            personality_dict[first_q] += 4 - choice
        elif choice > 4 :
            personality_dict[second_q] += choice - 4
    
    answer = []
    
    for i in range(4):
        first_p, second_p = personality_list[2*i:2*(i+1)]
        if personality_dict[first_p] >= personality_dict[second_p] :
            answer.append(first_p)
        else :
            answer.append(second_p)
    
    return ''.join(answer)
