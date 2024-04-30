computer_count, coupled_count = map(int,input().split())
graph = [[] for _ in range(computer_count+1)]
for _ in range(coupled_count):
    x, y = map(int, input().split())
    graph[x].append(y) # 양방향
    graph[y].append(x)
visited = [0 for _ in range(computer_count+1)]

def hack(v, count):
    visited[v] = 1
    for v2 in graph[v]:
        if visited[v2] == 0:
            visited[v]+=1
            count = hack(v2, count)
    return count

max_count = 0
for v in range(computer_count):
    if len(graph[v]) > 0 :
        max_count = max(max_count, hack(v, 0))

for v in range(computer_count):
    if visited[v] == max_count+1:
        print(v, ", ")
