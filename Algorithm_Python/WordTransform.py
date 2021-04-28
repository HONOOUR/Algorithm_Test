from collections import deque
import array


class WordTransform:
    def getShortestPath(self, begin: str, target: str, words: list) -> int:
        if words.count(target) < 1:
            return -1
        words.insert(0, begin)
        graph = []
        for v, w in enumerate(words):
            vertex = []
            for i in range(len(words)):
                if w == words[i]:
                    continue
                if sum(words[i][j] != w[j] for j in range(len(w))) == 1:
                    vertex.append(i)
            graph.append(vertex)

        answer = 0
        # queue = [(vertex, [path])]
        queue = deque([(0, [0])])
        while queue:
            v, p = queue.popleft()
            for i in graph[v]:
                path = list(p)
                path.append(i)
                queue.append((i, path))

            if words[i] == target:
                answer = len(p)
                break

        return answer


instance = WordTransform()
print(instance.getShortestPath("hit", "cog", [
      "hot", "dot", "dog", "lot", "log", "cog"]))
