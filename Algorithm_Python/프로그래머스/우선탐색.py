from collections import deque
def solution(n, computers):
    answer = 0
    graph = {}
    for i in range(n):
        graph.setdefault(i, [])
        for j, is_connected in enumerate(computers[i]):
            if i != j and is_connected == 1:
                graph[i].append(j)
    
    visited = set()
    for i in range(n):
        if i not in visited:
            answer += 1
        q = deque([i])
        while q:
            node = q.popleft()
            visited.add(node)
            for n in graph[node]:
                if n not in visited:
                    q.append(n)
        
    return answer

# solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])

def solution(n, computers):
    def dfs(node, visited):
        visited.add(node)
        for i in range(n):
            if computers[node][i] == 1 and i not in visited:
                dfs(i, visited)

    visited = set()
    answer = 0

    for i in range(n):
        if i not in visited:
            dfs(i, visited)
            answer += 1
    
    return answer

def solution(maps):
    is_solved = False
    min_count = 25
    def dfs(x, y, count, visited):
        visited.add((x,y))
        if x == len(maps[0])-1 and y == len(maps)-1:
            global is_solved
            global min_count
            is_solved = True
            min_count = min(min_count, count)
        
        for xd, yd in [[0,1], [0,-1], [-1,0], [1,0]]:
            if 0 <= x+xd < len(maps[0]) and 0 <= y+yd < len(maps) and (x+xd, y+yd) not in visited:
                if maps[y+yd][x+xd] == 1:
                    dfs(x+xd, y+yd, count+1, visited)
                    visited.remove((x+xd, y+yd))
    visited = set()
    dfs(0, 0, 0, visited)
    if is_solved:
        return min_count
    return -1
solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]])