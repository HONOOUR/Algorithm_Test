from collections import deque
M, N, H = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

ripe_tomato = deque([])
for y in range(N):
    for x in range(M):
        if tomato[y][x] == 1:
            ripe_tomato.append((y, x))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while ripe_tomato:
    y, x = ripe_tomato.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= ny < N and 0 <= nx < M:
            if tomato[ny][nx] == 0:
                tomato[ny][nx] = tomato[y][x] + 1
                ripe_tomato.append((ny, nx))  

answer = 0  
for y in range(N):
    for x in range(M):
        if tomato[y][x] == 0:
            print(-1)
            exit()
        answer = max(answer, tomato[y])

print(answer)


