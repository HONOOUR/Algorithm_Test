from collections import deque
TEST_CASE = int(input())
for _ in range(TEST_CASE):
    N = int(input())
    startY, startX = map(int, input().split())
    endY, endX = map(int, input().split())
    visited = set()

    # 이동 방향
    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]
    # bfs 빠른길 찾기

    queue = deque([])
    queue.append((startY, startX, 0))
    visited.add((startY, startX))
    while queue:
        y, x, count = queue.popleft()
        if y == endY and x == endX:
            print(count)
            break
        for i in range(8):
            if 0 <= y+dy[i] < N and 0 <= x+dx[i] < N:
                if (y+dy[i], x+dx[i]) not in visited:
                    queue.append((y+dy[i], x+dx[i], count+1))
                    visited.add((y+dy[i], x+dx[i]))