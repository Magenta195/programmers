###
# 베스트엘범
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/42579
# status : solved
# time : 00:16:43
###

from heapq import heappush, heappop

def solution(genres, plays):
    total_plays = list()
    genre_dict = dict()
    genre_count = 0
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genre_dict : 
            total_plays.append([0,genre])
            genre_dict[genre] = [genre_count, []]
            genre_count += 1
        
        genre_num = genre_dict[genre][0]
        total_plays[genre_num][0] += play
        heappush(genre_dict[genre][1], (-play, idx))
    
    answer = []
    total_plays.sort(reverse = True)
    for _, genre in total_plays :
        _genre_list = genre_dict[genre][1]
        if len(_genre_list) < 2:
            answer.append(_genre_list[0][1])
        else :
            for _ in range(2):
                _, idx = heappop(_genre_list)
                answer.append(idx)

    return answer
