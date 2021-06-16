from collections import deque


class Solutions:
    def getTime(self, n, start, end, roads, traps):
        answer = 0
        graph = {}
        for road in roads:
            p = road[0]
            q = road[1]
            s = road[2]
            if p in graph:
                graph[p].append((q, s))
            else:
                graph[p] = [(q, s)]

        queue = deque([(start, 0)])
        while queue:
            p, s = queue.popleft()
            if p in traps:
                for i in graph:
                    if graph[i][0][0] == p:
                        queue.append((i, s + graph[i][0][1]))

            else:
                for item in graph[p]:
                    queue.append((item[0], s+item[1]))

            if queue[0][0] == end:
                return queue[0][1]

        return answer


instance = Solutions()
n = 3
start = 1
end = 3
roads = [[1, 2, 2], [3, 2, 3]]
traps = [2]
instance.getTime(n, start, end, roads, traps)


def solution(n, k, cmd):
    answer = ''
    count = 0
    array = []
    
    while count < n:
        array.append("O")
        count += 1
    cstack = []
    cur_index = k

    for c in cmd:
        if c[0] == "U":
            cur_index -= int(c[2])
        elif c[0] == "D":
            cur_index += int(c[2])
        elif c[0] == "C":
            array[cur_index] = "X"
            cstack.append(cur_index)
            if cur_index == n-1:
                cur_index -= 1
            else:
                cur_index += 1
        else:  # "z"
            removed_index = cstack.pop()
            array[removed_index] = "O"

    for item in array:
        answer += item

    return answer