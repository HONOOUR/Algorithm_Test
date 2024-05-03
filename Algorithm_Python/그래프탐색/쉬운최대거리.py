from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
queue = deque([])
for i in range(n):
    line = list(map(int, input().split()))
    graph[i].extend(line)
    if line.count(2) == 1:
        queue.append((i,line.index(2)))
        graph[i][line.index(2)] = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


while queue:
    x, y = queue.popleft()
    visited[y][x] = 1
    if x == m-1 and y == n-1:
        break
    for i in range(4):
        if x+dx[i] == 0 and y+dy[i] == 0:
            continue
        if 0 <= x+dx[i] < m and 0 <= y+dy[i] < n and graph[y+dy[i]][x+dx[i]] == 1:
            graph[y+dy[i]][x+dx[i]] = graph[y][x] + 1
            queue.append((x+dx[i],y+dy[i]))

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and graph[i][j] != 0:
            graph[i][j] = -1
        print(graph[i][j], end=' ')
    print()