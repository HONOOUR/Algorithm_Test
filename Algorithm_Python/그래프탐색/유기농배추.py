<<<<<<< Updated upstream
# https://www.acmicpc.net/problem/1012

# 상하좌우 탐색 -> 더 이상 배추가 없을 때 정지 -> 카운트 1 증가

test_count = int(input())
=======
from collections import deque
def bfs(n, m):
    queue = deque([(n, m)])
    visited[m][n] = 1
    while queue:
        n, m = queue.popleft()
        # 상하좌우 -> 큐 -> 큐
        for dx, dy in [[0,1], [0,-1], [-1,0], [1,0]]:
            if 0 <= m + dy < len(graph) and 0 <= n + dx < len(graph[0]):
                if graph[m+dy][n+dx] == 1 and visited[m+dy][n+dx] == 0:
                    queue.append((m+dy, n+dx))
                    visited[m+dy][n+dx] = 1

test_count = int(input())
for _ in range(test_count):
    n, m, count = map(int, input().split())
    graph = [[0 for _ in range(n)] for _ in range(m)]
    visited = [[0 for _ in range(n)] for _ in range(m)]
    target = []
    for _ in range(count):
        n, m = map(int, input().split())
        graph[m][n] = 1
        target.append([n, m])
    answer = 0
    for n, m in target:
        if visited[m][n] != 1:
            answer += 1
            bfs(n, m)
    print(answer)
>>>>>>> Stashed changes
