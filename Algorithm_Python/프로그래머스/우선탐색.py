from collections import deque
def solution(n, computers):
    answer = 0
    graph = {}
    for i in range(n):
        graph.setdefault(i, [])
        for j, is_connected in enumerate(computers[i]):
            if i != j and is_connected == 1:
                graph[i].append(j)
    
    visited = set()
    for i in range(n):
        if i not in visited:
            answer += 1
        q = deque([i])
        while q:
            node = q.popleft()
            visited.add(node)
            for n in graph[node]:
                if n not in visited:
                    q.append(n)
        
    return answer

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])