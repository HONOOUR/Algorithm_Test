# 상하좌우 모두 방문하지 않은 곳을 확인하고 중앙에 꽃을 심는다
# 모든 노드를 방문해서 최대로 많이 심을 수 있는 경우를 찾는다
# 중앙을 포함한 다섯개의 노드에 있는 값을 더한다
N = int(input())
graph = [[] for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    line = list(map(int, input().split(' ')))
    graph[i].extend(line)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
answer = 0

def flower(x, y, price):
    isUsed = False
    for i in range(4):
        if 0 <= x+dx[i] < N and 0 <= y+dy[i] < N and visited[y+dy[i]][x+dx[i]] == 0:
            price += graph[y+dy[i]][x+dx[i]]
        else:
            isUsed = True
    if not isUsed:
        visited[y][x] = 1
        answer += price
        for i in range(4):
            visited[y+dy[i]][x+dx[i]] = 1
        
  
for x in range(N):
    for y in range(N):
        if visited[y][x] == 0:
            flower(x, y, graph[y][x])