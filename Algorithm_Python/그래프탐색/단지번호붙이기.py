N = int(input())
graph = [[] for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    graph[i].extend(list(map(int, input())))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(y, x, count):
    visited[y][x] = 1
    for i in range(4):
        if 0 <= x+dx[i] < N and 0 <= y+dy[i] < N and graph[y+dy[i]][x+dx[i]] == 1 and visited[y+dy[i]][x+dx[i]] == 0:
            count = dfs(y+dy[i], x+dx[i], count+1)
    return count 

answers = []
for y in range(N):
    for x in range(N):
        if visited[y][x] == 0 and graph[y][x] == 1:
            answers.append(dfs(y, x, 1))
answers.sort()
print(len(answers))
for answer in answers:
    print(answer)
