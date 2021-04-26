class network:
    def getNetwork(self, n: int, computers: list) -> int :
        vertex = {}
        for i, computer in enumerate(computers):
            for index, com in enumerate(computer):
                if com == 1 and index != i:
                    if i in vertex:
                        vertex[i].append(index)
                    else:
                        vertex[i] = [index]

        visited = []
        for i in range(n):
            visited.append(False)

        visited = network.dfs(self, vertex, 0, visited)
        answer = visited.count(False)

        return answer + 1


def dfs(self, vertices: dict, index: int, visited: list) -> list:
    visited[index] = True
    for node in vertices[index]:
        if visited[node] == False:
            network.dfs(self, vertices, node, visited)

    return visited

instance = network()
print(instance.getNetwork(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
