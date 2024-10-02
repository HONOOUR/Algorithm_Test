# https://school.programmers.co.kr/learn/courses/30/lessons/42746
from functools import cmp_to_key
def compare(x, y):
    if x + y > y + x:
        return -1
    else:
        return 1
    
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    largest_num = ''.join(numbers)
    if largest_num[0] == '0':
        return 0
    else:
        largest_num

# https://school.programmers.co.kr/learn/courses/30/lessons/42747?language=python3
def solution(citations):
    citations.sort()
    h_index = citations[0]
    n = len(citations)
    for i in range(n):
        h_index = n-i # 5-2 = 3 개
        if citations[i] >= h_index:
            return h_index
    return 0