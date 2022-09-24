###
# 매칭 점수
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/42893
# status : solved
# time : 01:34:30
###

import re
from collections import defaultdict

def solution(word, pages):
    word = word.lower()

    link_dict = defaultdict(list)
    score_dict = defaultdict(list)
    for idx, page in enumerate(pages) :
        _page = page.lower()
        url = re.findall(r"<meta property=\"og:url\" content=\"(https://\S+)\"", page)
        link = re.findall(r"<a href=\"(https://\S+)\"", page)
        words = re.findall("[^a-z]*([a-z]+)", _page)
        word_cnt = 0
        for _words in words :
            if _words == word :
                word_cnt += 1

        link_dict[url[0]] = link[:]
        score_dict[url[0]] = [idx, word_cnt, word_cnt]
        
    for url, link in link_dict.items():
        if not link :
            continue
        base_score = score_dict[url][1]
        link_score = base_score / len(link)
        for _link in link :
            if _link in score_dict :
                score_dict[_link][2] += link_score
                
    score_list = list(score_dict.values())
    score_list.sort(key = lambda x : (x[2], -x[0]))
    return score_list[-1][0]
