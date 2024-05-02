from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    graph[i].extend(list(map(int, input())))
answer = (n-1)*(m-1)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

queue = deque([()])
queue.append((0,0))
while queue:
    x, y = queue.popleft()
    if x == m-1 and y == n-1:
        print(graph[n-1][m-1])
        break
    for i in range(4):
        if 0 <= x+dx[i] < m and 0 <= y+dy[i] < n and graph[y+dy[i]][x+dx[i]] == 1:
            graph[y+dy[i]][x+dx[i]] = graph[y][x] + 1


