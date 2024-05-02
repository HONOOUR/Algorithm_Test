
n = int(input())

# 그래프 만들기
graph = [[] for _ in range(n+1)]
for _ in range(n-1):  # 간선수는 n-1개
    x, y = map(int, input().split())  # [[1,2], [2,3] .....]
    graph[x].append(y)
    graph[y].append(x)
visited = [0] * (n+1) #방문여부 대신, 부모를 담을 변수


# dfs 함수
def dfs(v):
   # 현재 V와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:  # 방문하지 않은 노드라면
            # visited를 1이 아닌, 탐색을 시작한 값을 넣어준다 dfs는 항상 부모에서 자식으로 이동한다.
            visited[i] = v
            dfs(i)  # 해당 노드를 시작 노드로 dfs

dfs(1) #항상 1이 시작노드

# visited 출력
for i in range(2, n+1):
    print(visited[i])