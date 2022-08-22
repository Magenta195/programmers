###
# n^2 배열 자르기
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/87390
# status : solved
# time : 00:11:14
###

def solution(n, left, right):
    answer = []
    left_col, left_row = left // n, left % n
    right_col, right_row = right // n, right % n
    if left_col == right_col : 
        new_list = [left_col+1 if left_col+1 > row else row for row in range(1,n+1)]
        new_list = new_list[left_row:right_row+1]
        answer = new_list
    else :
        for col in range(left_col, right_col + 1):
            new_list = [col+1 if col+1 > row else row for row in range(1,n+1)]
            if col == left_col : new_list = new_list[left_row:]
            if col == right_col : new_list = new_list[:right_row+1]
            answer.extend(new_list)
    
    return answer
