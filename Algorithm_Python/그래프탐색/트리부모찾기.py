# https://www.acmicpc.net/problem/11725
# 방문 여부를 확인할 떼 부모 노드를 넣는다
# 부모 : 자식 = 1 : N
# 리미트 지정 안한 경우 - 런타임 에러 발생
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [0 for _ in range(n+1)]


def dfs(v):
    for u in graph[v]:
        if visited[u] == 0:
            visited[u] = v
            dfs(u)
dfs(1)

for i in range(2, n+1):
    print(visited[i])