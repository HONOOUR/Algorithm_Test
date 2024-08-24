from collections import Counter
def makeAnagram(a, b):
    first = list(a)
    second = list(b)
    first_dic = Counter(first)
    second_dic = Counter(second)
    answer = 0
    for value in (first_dic - second_dic).values():
      answer += value
    for value in (second_dic - first_dic).values():
      answer += value
    return answer
    
makeAnagram('fcrxzwscanmligyxyvym', 'jxwtrhvujlmrpdoqbisbwhmgpmeoke')

def isValid(s):
    s_dict = Counter(s)
    s_frequency_dict =Counter(s_dict.values())
    if len(s_frequency_dict) == 1:
        return 'YES'
    elif len(s_frequency_dict) > 2:
        return 'NO'
    else:
        keys = list(s_frequency_dict.keys())
        values = sorted(list(s_frequency_dict.values()))
        if values[0] == 1 and abs(keys[0]-keys[1]) == 1:
            return 'YES'
        else: 
            return 'NO'

isValid('aabbcd')