# 모든 노드가 신호를 받는데 걸리는 시간
# 모든 노드가 도달할 수 있는지 여부
import collections
import heapq


class NetworkDelayTime:
    def getNetworkDelayTime(self, network: [[]], N: int, start_node: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, w in network:
            graph[u].append((v, w))  # graph[2] = (1, 1)

        Q = [{0, start_node}]
        dist = collections.defaultdict(int)

        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        if len(dist) == N:
            return max(dist.values())


network = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
instance = NetworkDelayTime()
instance.getNetworkDelayTime(network, 4, 2)
