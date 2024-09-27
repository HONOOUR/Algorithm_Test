# def checkMagazine(magazine, note):
#       # create hashmap with magazine and check if the key has the value
#       magazine_dict = {}
#       for key in magazine:
#           if key in magazine_dict.keys():
#               magazine_dict[key] += 1
#           else:
#               magazine_dict[key] = 1
      
#       for key in magazine_dict.keys():
#           for _ in range(magazine_dict.get(key)):
#               if key in note:
#                   note.remove(key)
          
#       if len(note) == 0:
#           print('Yes')
#       else:
#           print('No')
# time exeeded
from collections import Counter          
def checkMagazine(magazine, note):
    magazine_dic = Counter(magazine)
    note_dic = Counter(note)
    if len(note_dic - magazine_dic) > 0:
        print('No')
    else:
        print('Yes')
          
# https://school.programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    answer = ''
    participant_counter = Counter(participant)
    completion_counter = Counter(completion)
    answer_counter = participant_counter - completion_counter
    answer = list(answer_counter.keys())[0]
    return answer


checkMagazine({"give", "me", "one", "grand", "today", "night"}, {"give", "one", "grand", "today"})