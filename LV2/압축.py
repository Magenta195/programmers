###
# 압축
# problem : https://school.programmers.co.kr/learn/courses/30/lessons/17684
# status : solved
# time : 00:09:02
###


def solution(msg):
  A_val = ord('A')
  chr_dict = { chr(key) : key - A_val + 1 for key in range(A_val, A_val + 26)}
  chr_idx = 26

  length = len(msg)
  idx = 0
  answer = []
  while idx < length :
      _idx = idx + 1
      while _idx < length + 1 :
          _msg = msg[idx:_idx]
          if _msg not in chr_dict :
              answer.append( chr_dict[_msg[:-1]] )
              chr_dict[_msg] = chr_idx + 1
              chr_idx += 1
              idx = _idx - 1
              break
          elif _idx == length :
              answer.append( chr_dict[_msg] )
              idx = _idx
              break
          _idx += 1

  return answer
