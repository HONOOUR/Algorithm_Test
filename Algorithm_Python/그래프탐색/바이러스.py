computer_count = int(input())
coupled_count = int(input())
graph = [[] for _ in range(computer_count+1)]
for _ in range(coupled_count):
    x, y = map(int, input().split())
    graph[x].append(y) # 양방향
    graph[y].append(x)
visited = [0 for _ in range(computer_count+1)]

def virus_dfs(start):
    visited[start] = 1
    for v in graph[start]:
        if visited[v] == 0:
            virus_dfs(v)
virus_dfs(1)
print(visited.count(1)-1) # 1번 컴퓨터 개수 1개

# 지역변수 사용
def virus_dfs(start, count):
    visited[start] = 1
    for v in graph[start]:
        if visited[v] == 0:
            count = virus_dfs(v, count+1)
    return count
print(virus_dfs(1, 1))

