import math
from collections import deque
import copy


def solution(keymap, targets):
    answer = []
    keys_dic = {}
    for keys in keymap:
        press_count = 1
        for key in keys:
            if key in keys_dic:
                if keys_dic[key] > press_count:
                    keys_dic[key] = press_count
            else:
                keys_dic[key] = press_count
            press_count += 1

    for target in targets:
        total = 0
        for key in target:
            if key in keys_dic:
                total += keys_dic[key]
            else:
                total = -1
                break
        answer.append(total)
    return answer


solution(["ABACD", "BCEFD"], ["VVAB", "AABB"])


def solution(n, m, section):
    answer = 1
    point = section[0]
    for s in section[1:]:
        if s >= point+m:
            point = s
            answer += 1
    return answer


solution(4, 1, [1, 2, 3, 4])

min_move = 0


def dfs(r, c, map, visited, move):
    if map[r][c] == "E":
        global min_move
        min_move = move
        return

    for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        if 0 <= r+dy < len(map) and 0 <= c+dx < len(map[0]):
            if map[r+dy][c+dx] == "X":
                continue
            if visited[r+dy][c+dx] == 0:
                visited[r+dy][c+dx] = 1
                dfs(r+dy, c+dx, map, visited, move+1)


def solution(maps):
    global min_move
    r, c = 0, 0
    map = []
    for i in range(len(maps)):
        row = []
        for j in range(len(maps[i])):
            row.append(maps[i][j])
            if maps[i][j] == "S":
                r, c = i, j
        map.append(row)
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]

    dfs(r, c, map, visited, 0)
    if min_move == 0:
        return -1
    return min_move


def solution(maps):
    sr, sc = 0, 0
    lr, lc = 0, 0
    map = []
    for i in range(len(maps)):
        row = []
        for j in range(len(maps[i])):
            row.append(maps[i][j])
            if maps[i][j] == "S":
                sr, sc = i, j
            if maps[i][j] == "L":
                lr, lc = i, j
        map.append(row)
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    temp_visited = copy.deepcopy(visited)
    queue = deque([(sr, sc, 0)])
    l_move = 0
    while queue:
        r, c, move = queue.popleft()
        temp_visited[r][c] = 1
        for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            if 0 <= r+dy < len(map) and 0 <= c+dx < len(map[0]):
                if map[r+dy][c+dx] == "X" or temp_visited[r+dy][c+dx] == 1:
                    continue
                if map[r+dy][c+dx] == "L":
                    l_move = move + 1
                    break
                queue.append((r+dy, c+dx, move+1))

    if l_move == 0:
        return -1

    e_move = 0
    queue = deque([(lr, lc, 0)])
    while queue:
        r, c, move = queue.popleft()
        visited[r][c] = 1
        for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            if 0 <= r+dy < len(map) and 0 <= c+dx < len(map[0]):
                if map[r+dy][c+dx] == "X" or visited[r+dy][c+dx] == 1:
                    continue
                if map[r+dy][c+dx] == "E":
                    return l_move + move + 1
                queue.append((r+dy, c+dx, move+1))

    if e_move == 0:
        return -1


# print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))

def solution(maps):
    answer = []
    map = []
    for i in range(len(maps)):
        row = []
        for j in range(len(maps[i])):
            row.append(maps[i][j])
        map.append(row)
    visited = [[0 for _ in range(len(map[0]))] for _ in range(len(map))]

    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] != "X" and visited[r][c] != 1:
                food = int(map[r][c])
                queue = [(r, c)]
                visited[r][c] = 1
                while len(queue) > 0:
                    rr, cc = queue.pop(0)
                    for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                        if 0 <= rr+dy < len(map) and 0 <= cc+dx < len(map[0]):
                            if map[rr+dy][cc+dx] != "X" and visited[rr+dy][cc+dx] != 1:
                                queue.append((rr+dy, cc+dx))
                                visited[rr+dy][cc+dx] = 1
                                food += int(map[rr+dy][cc+dx])
                answer.append(food)
    if len(answer) == 0:
        return [-1]
    answer.sort()
    return answer


# solution(["X591X", "X1X5X", "X231X", "1XXX1"])


def solution(numbers):
    answer = []
    test = numbers.copy()
    test.sort()
    for num in numbers:
        idx = test.index(num)
        while idx < len(numbers)-1:
            if num == test[idx+1]:
                idx += 1
            else:
                break
        if idx < len(numbers)-1:
            answer.append(test[idx+1])
        else:
            answer.append(-1)

    return answer


def solution(x, y, n):
    queue = deque([(0, [x+n, x*2, x*3], 0)])
    while len(queue) > 0:
        target, nums, count = queue.popleft()
        if target == y:
            return count
        for num in nums:
            if target+num <= y:
                queue.append((target+num, [x+n, x*2, x*3], count+1))
    return -1


def solution(weights):
    answer = 0
    i = 0
    j = i+1
    while i <= len(weights)-2:
        is_found = False
        for n in range(2, 5):
            if weights[i]*n == weights[j]*2:
                answer += 1
                is_found = True
                continue

            if weights[i]*n == weights[j]*3:
                answer += 1
                is_found = True
                continue

            if weights[i]*n == weights[j]*4:
                answer += 1
                is_found = True
                continue
            if is_found:
                break
        if j < len(weights)-1:
            j += 1
        else:
            i += 1
            j = i+1

        # for m in range(2, 5):
        #     for n in range(2, 5):
        #         if weights[i]*m == weights[j]*n:
        #             answer += 1
        #             is_found = True
        #             break
        #     if is_found:
        #         break
        # if j < len(weights)-1:
        #     j += 1
        # else:
        #     i += 1
        #     j = i+1
    return answer


def check(cols, n):
    table = [[0 for _ in range(n)] for _ in range(n)]
    for row, col in enumerate(cols):
        for dx, dy in [(-1, 1), (0, 1), (1, 1)]:
            c = col
            r = row
            while 0 <= c+dx < n and 0 <= r+dy < n:
                c += dx
                r += dy
                table[r][c] = 1
    new_row = len(cols)
    cols = []
    for i in range(n):
        if table[new_row][i] == 0:
            cols.append(i)
    return cols


def solution(n):
    answer = 0
    queue = deque([])
    for i in range(n):
        queue.append([i])

    while len(queue) > 0:
        cols = queue.popleft()
        if len(cols) == n:
            answer += 1
            continue

        new_cols = check(cols, n)
        if len(new_cols) == 0:
            continue

        for col in new_cols:
            temp = copy.deepcopy(cols)
            temp.append(col)
            queue.append(temp)

    return answer


# solution(4)


def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        endX = ball[0]
        endY = ball[1]
        first = math.sqrt((abs(startX-endX)/2)**2+startY**2) + \
            math.sqrt((abs(startX-endX)/2)**2+endY**2)
        second = math.sqrt((abs(startX-endX)/2)**2+abs(n-startY)**2) + \
            math.sqrt((abs(startX-endX)/2)**2+abs(n-endY)**2)
        min_dis = min(first, second)
        answer.append(min_dis**2)
    return answer


def solution(s):
    answer = True
    chars = list(s)
    queue = deque(chars)
    stack = []
    while len(queue) > 0:
        char = queue.popleft()
        if len(stack) == 0:
            stack.append(char)
        else:
            if stack[-1] == "(" and char == ")":
                stack.pop()
            elif stack[-1] == "{" and char == "}":
                stack.pop()
            elif stack[-1] == "[" and char == "]":
                stack.pop()
            else:
                stack.append(char)

    if len(stack) > 0:
        return False
    return answer


# solution("([]){}")


def solution(numbers):
    k = len(numbers) - 1
    round = 0
    if len(numbers) == 1:
        numbers[0] += 1
        return numbers

    while k > 0:
        if numbers[k] == 9:
            round = 1
            numbers[k] = 0
            k -= 1
        else:
            numbers[k] = numbers[k]+1
            break
    if round == 1:
        numbers[0] = numbers[0]+1
    print(numbers)


# solution([1, 3, 9, 9])

def solution(inputs, pattern):
    upper_str = ""
    upper_pattern = ""
    inputs = "BucketPlace"
    inputs.lower
    for s in inputs:
        if s.isupper:
            upper_str += s
    is_upper_pattern = False
    patterns = list(pattern)
    for i in range(len(patterns)):
        if patterns[i].isupper:
            upper_pattern += patterns[i]
        else:
            is_upper_pattern = False
    max(1, 3)
    if is_upper_pattern:
        if upper_str == upper_pattern:
            print(True)


def calculateScore(text, prefixString, suffixString):
    text = "nothing"
    prefixString = "bruno"

    prefix_length = 0
    prefix_selected = ""
    for i in range(len(prefixString)-1, 0, -1):
        prefix = prefixString[i:]
        if text[:len(prefix)] == prefix:
            prefix_length = max(prefix_length, len(prefix))
            prefix_selected = prefix

    suffix_length = 0
    suffix_selected = ""
    for i in range(len(suffixString)):
        suffix = suffixString[:i+1]
        if text[len(text)-i-1:] == suffix:
            suffix_length = max(suffix_length, len(suffix))
            suffix_selected = suffix

    if len(text) <= prefix_length + suffix_length:
        return text
    elif prefix_length > suffix_length:
        return prefix_selected
    elif suffix_length > prefix_length:
        return suffix_selected
    else:

        if ord(prefix_selected[0]) < ord(suffix_selected[0]):
            return prefix_selected
        else:
            return suffix_selected


# calculateScore("nothing", "bruno", "ingenious")


def separate_number_and_unit(string):
    num = ""
    unit = ""
    for c in string:
        if c.isdigit():
            num += c
        else:
            unit += c
    return int(num), unit


print(separate_number_and_unit("4KB"))  # 출력 결과: (4, 'KB')
print(separate_number_and_unit("56B"))  # 출력 결과: (56, 'B')


def solution(N, board):
    K = N//2
    min_move = 1000*(K+1)
    visited = []
    graph = []
    for i in range(N):
        visited.append([0 for _ in range(N)])
        temp = []
        for j in range(N):
            temp.append(board.pop(0))
            if i == j:
                visited[i][j] = 1
        graph.append(temp)

    def dfs(y, x, total, visited):
        for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            if y+dy < 0 or y+dy > N or x+dx < 0 or x+dx > N:
                min_move = min(min_move, total)
                return
            if visited[y+dy][x+dx] == 0:
                visited[y+dy][x+dx] = 1
                dfs(y+dy, x+dx, total+graph[y+dy][x+dx], visited)
    dfs(K, K, 0, visited)


# solution(5, [4, 4, 4, 4, 5, 6, 7, 3, 9, 6, 9, 4,
#          5, 2, 4, 9, 4, 5, 2, 4, 9, 4, 5, 2, 4])


def solution(arr):
    i = 0
    j = 1
    count = 0
    X = (arr[0]-arr[1])
    temp_count = 1
    while i < j and j < len(arr)-1:
        i += 1
        j += 1
        if X == (arr[i]-arr[j]):
            temp_count += 1
        else:
            count = max(count, temp_count)
            temp_count = 1
            X = (arr[i]-arr[j])
    print(max(count, temp_count))


solution([2, 3, 4, -1, -6, -11, 1])
