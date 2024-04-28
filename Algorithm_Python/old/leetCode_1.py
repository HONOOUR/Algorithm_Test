from collections import deque


# def solution(A, B):
#     # write your code in Python 3.6
#     C = []
#     for i in range(len(A)):
#         if A[i] > B[i]:
#             C.append(A[i])
#         else:
#             C.append(B[i])

#     C.sort()
#     start = C[0]+1
#     for num in C[1:]:
#         if start == num:
#             start += 1
#         else:
#             return start


# solution([1, 2, 4, 3], [1, 3, 2, 3])


# def solutions(S):
#     V = int(S, 2)
#     count = 0
#     while V != 0:
#         if V % 2 == 0:
#             V //= 2
#         else:
#             V -= 1
#         count += 1
#     return count


# solutions('011100')


def solutions(S):
    substrings = []
    start = 0
    end = 0
    strings = list(S)
    for s in S:
        if strings.count(s.upper()) > 0 and strings.count(s.lower()) > 0:
            end += 1
        else:
            temp = S[start:end]
            substrings.append(temp)
            start = end+1
            end = start

    if end == len(S):
        substrings.append(S[start:end])

    length = 0
    for string in substrings:
        count = len(string)
        temp = 0
        for s in string:
            if strings.count(s.upper()) > 0 and strings.count(s.lower()) > 0:
                temp += 1
        if count == temp:
            length = max(length, count)

    if length == 0 or length == 1:
        return -1
    else:
        return length


solutions("AcZCbaBz")

# https://leetcode.com/problems/climbing-stairs/
# no order
answer_stairs = 0


def dfs_steps(sum_steps, visited, num_stairs):
    if sum_steps == num_stairs:
        global answer_stairs
        answer_stairs += 1
    elif sum_steps > num_stairs:
        return

    for i in range(1, num_stairs):
        if visited[i] == 1:
            continue

        visited[i] = 1
        dfs_steps(sum_steps+i, visited, num_stairs)
        visited[i] = 0


def getNumOfWays(num_stairs):
    visited = [0 for _ in range(num_stairs+1)]
    dfs_steps(0, visited, num_stairs)
    global answer_stairs
    return answer_stairs


getNumOfWays(3)
