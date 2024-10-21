# https://school.programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    answer = []
    arr_1 = [1, 2, 3, 4, 5]
    arr_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    arr_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    arr_count = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == arr_1[i%5]:
            arr_count[0] += 1
        if answers[i] == arr_2[i%8]:
            arr_count[1] += 1
        if answers[i] == arr_3[i%10]:
            arr_count[2] += 1
    max_count = max(arr_count)
    for i in range(len(arr_count)):
        if max_count == arr_count[i]:
            answer.append(i+1)
    return answer
  
from itertools import permutations

def solution(numbers):
    numbers = list(numbers)
    prime_numbers = set()
    for count in range(1, len(numbers)+1):
        for nums in permutations(numbers, count):
            temp = ''.join(nums)
            num = int(temp)
            is_prime = True
            for i in range(2, int(num**0.5+1)): # root 사용 해서 소수 체크
                if num % i == 0:
                    is_prime = False
            if is_prime and num >= 2:
                prime_numbers.add(num)
    return len(prime_numbers)
  
solution("17")

# https://school.programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    answer = []
    # brown_y = yellow_y + 2
    # brown_x = yellow_x + 2
    
    for yellow_x in range(1, yellow+1):
        if yellow % yellow_x == 0:
            yellow_y = yellow // yellow_x
            if ((yellow_x+2)+(yellow_y+2))*2== brown+4:
                return [yellow_y+2, yellow_x+2]

# https://school.programmers.co.kr/learn/courses/30/lessons/87946
from itertools import permutations
def solution(k, dungeons):
    max_count = -1
    for arr in permutations(dungeons, len(dungeons)):
        count = 0
        start_power = k
        for min_power, power in arr:
            if start_power >= min_power:
                start_power -= power
                count += 1
        max_count = max(max_count, count)
    return max_count

solution(80, [[80,20],[50,40],[30,10]])

def solution(n, wires):
    min_value = n
    for i in range(len(wires)):
        a = [wires[i][0]]
        b = [wires[i][1]]
        for j in range(len(wires)):
            if i == j:
                continue
            if wires[j][0] in a:
                a.append(wires[j][1])
            elif wires[j][1] in a:
                a.append(wires[j][0])
            elif wires[j][0] not in b:
                b.append(wires[j][0])
            else:
                b.append(wires[j][1])
        min_value = min(min_value, abs(len(a)-len(b)))
    return min_value

solution(9, [[4,7], [1,3],[2,3],[3,4],[4,5],[4,6],[7,8],[7,9]])

def solutions(scores):
    answer = [0 for _ in range(len(scores))]
    score_0 = 0
    score_1 = 0
    for i in range(len(scores)):
        score_0 += scores[i][0]
        score_1 += scores[i][1]
        scores[i].append(scores[i][0]+scores[i][1])
        scores[i].append(i)

    score_index = 0
    if score_0 > score_1:
        score_index = 1
    scores_sorted = sorted(scores, key=lambda x: (x[2], x[score_index], -x[3]))
    for i, score in enumerate(scores_sorted):
        index = score[3]
        answer[index] = i+1
    
    return answer

# solutions([[85, 90], [91, 87], [88, 87]])

def solution(square, k):
    answer = [[]]
    for _ in range(k):
        for i in range(len(square)):
            square[i].extend(square[i][::-1])
        for i in range(len(square)-1, -1, -1):
            square.append(square[i])
    return square

answer = 0

def dfs(grid, visited, x, y, path_sum):
    if (x, y) in visited:
        return
    if x == len(grid[0])-1 and y == len(grid)-1:
        global answer
        answer = min(answer, path_sum)
    visited.add((x,y))

    for dx, dy in [[0,1],[1,0],[0,-1],[-1,0]]:
        if 0 <= x+dx < len(grid[0]) and 0 <= y+dy < len(grid):
            if (x+dx, y+dy) not in visited:
                dfs(grid, visited, x+dx, y+dy, path_sum+grid[y+dy][x+dx])
    visited.remove((x,y))

def solutions(grid):
    global answer
    answer = len(grid[0])*len(grid)*1000

    x = y = 0
    visited = set()
    dfs(grid, visited, x, y, grid[y][x])
    print(answer)

solutions([[1, 8, 3, 2], [7, 4, 6, 5]])

answer = 0
def dfs(board, y, x, visited, count):
    visited.add((x, y))
    global answer
    answer = max(answer, count)
    for dx, dy in [[0,1],[1,0],[0,-1],[-1,0]]:
        if 0 <= x+dx < len(board[0]) and 0 <= y+dy < len(board):
            if (x+dx, y+dy) not in visited:
                if board[y][x] < board[y+dy][x+dx]:
                    dfs(board, y+dy, x+dx, visited, count+1)

def solution(board):
    global answer
    for y in range(len(board)):
        for x in range(len(board[0])):
            visited = set()
            dfs(board, y, x, visited, 1) 
    return answer

is_solved = False
min_count = 25

def solution(maps):
    visited = set()
    def dfs(x, y, count):
        visited.add((x,y))
        if x == len(maps[0])-1 and y == len(maps)-1:
            global is_solved
            is_solved = True
            global min_count
            min_count = min(min_count, count)
        
        for xd, yd in [[0,1], [0,-1], [-1,0], [1,0]]:
            if 0 <= x+xd < len(maps[0]) and 0 <= y+yd < len(maps) and (x+xd, y+yd) not in visited:
                if maps[y+yd][x+xd] == 1:
                    dfs(x+xd, y+yd, count+1)
                    visited.remove((x+xd, y+yd))
    dfs(0, 0, 1)
    if is_solved:
        return min_count
    return -1

def solution(maps):
    if len(maps) == 1 and len(maps[0]) == 1:
        return 1
    row_len = len(maps)
    vec_len = len(maps[0])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 맵 받기
    def bfs():
        queue = deque()
        queue.append((0, 0))
        
        while queue:
            row, vec = queue.popleft()
            if (row, vec) == (row_len - 1, vec_len - 1):
                return maps[row][vec]
            for (y, x) in zip(dy, dx):
                new_row = row + y
                new_vec = vec + x
                if new_row < 0 or new_row >= row_len or \
                    new_vec < 0 or new_vec >= vec_len or \
                    maps[new_row][new_vec] == 0 or \
                    (maps[new_row][new_vec] != 1 and 
                     maps[new_row][new_vec] <= maps[row][vec] + 1):
                    continue
                maps[new_row][new_vec] = maps[row][vec] + 1
                queue.append((new_row, new_vec))
        return -1

    return bfs()
