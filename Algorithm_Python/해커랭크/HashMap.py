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

def solution(phone_book):
    # create dict for lookup
    phone_book_dict = {}
    for number in phone_book:
        phone_book_dict[number] = number
    
    # create prefix
    for numbers in phone_book:
        prefix_num = ""
        for num in numbers:
            prefix_num += num
            if prefix_num != numbers and prefix_num in phone_book_dict:
                return False
    return True

checkMagazine({"give", "me", "one", "grand", "today", "night"}, {"give", "one", "grand", "today"})

# https://school.programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    answer = 1
    clothes_dict = {}
    for item, category in clothes:
        clothes_dict.setdefault(category, [])
        clothes_dict[category].append(item)
    for items in clothes_dict.values():
        # 0 ~ 모두 선택하는 경우의 수 (n개+1)*(m개+1) -> 모든 카테고리 0 ~ 모두 선택 경우
        answer *= (len(items)+1)
    # 그러나 모두 선택하지 않는 경우 제거 
    return answer-1

def solution(genres, play):
    answer = []
    genres_dict = {} # genres_dict['classic'] = [(0, 800), ()]
    for index, genre in enumerate(genres):
        genres_dict.setdefault(genre, [])
        genres_dict[genre].append((index, play[index]))
    genres_total_play_dict = {} # genres_total_play_dict['classic'] = 1500
    for genre in genres_dict.keys():
        genres_total_play_dict.setdefault(genre, 0)
        for index, plays in genres_dict[genre]:
            genres_total_play_dict[genre] += plays
    genres_sorted_dict = sorted(genres_total_play_dict.items(), key=lambda item: -item[1])
    for genre, total_plays in genres_sorted_dict:
        palys_sorted_dict = sorted(genres_dict[genre], key=lambda x:(-x[1], x[0]))
        answer.append(palys_sorted_dict[0][0])
        if len(genres_dict[genre]) > 1:
            answer.append(palys_sorted_dict[1][0])
    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])

def solution(numbers):
    numbers = list(map(str, numbers))
    temp_num = ''
    for number in numbers:
        temp_num += number
        number += temp_num
        if int(number) > int(temp_num):
            temp_num = number
    return temp_num