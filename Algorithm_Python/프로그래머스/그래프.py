# https://school.programmers.co.kr/learn/courses/30/lessons/43163
from collections import deque, Counter

def solution(begin, target, words):
    visited = set()
    queue = deque([(begin, 0)])
    while queue:
        # 1. 한개의 단어만 다른지 체크
        word_begin, count = queue.popleft()
        if word_begin == target:
            return count
        if count > len(words):
            break
        visited.add(word_begin)
        for word in words:
            if word not in visited:
                if sum([1 for a, b in zip(word_begin, word) if a != b]) == 1:
                    # 2. 큐에 넣기 (word, count+1)
                    queue.append((word, count+1))

    return 0