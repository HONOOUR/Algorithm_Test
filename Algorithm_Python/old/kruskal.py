# 최소비용신장트리
def getParents(parents, node):
    if parents[node] == node:
        return node
    else:
        getParents(parents, parents[node])


def kruskal(graph, node_counts):
    # 제일 작은 값 부터 선택하고
    # 사이클이 생기는지 확인 (부모테이블에 부모가 같은지)
    # 제일 작은 부모로 업데이트
    parents = [[x] for x in range(0, node_counts+1)]
    sorted_graph = sorted(graph, key=lambda value: graph[2])
    values = 0
    for i in range(len(sorted_graph)):
        node1, node2, value = sorted_graph[i]
        if node1 < node2:
            if getParents(parents, node1) != getParents(parents, node2):
                parents[node2] = parents[node1]
                values += value
            else:
                # 사이클
                continue
    print(values)


# graph = [[노드, 노드, 값]]
graph = [[1, 7, 12], [1, 4, 28], [1, 2, 67], [1, 5, 17], [2, 4, 24], [
    2, 5, 62], [3, 5, 20], [3, 6, 37], [4, 7, 13], [5, 6, 45], [5, 7, 73]]
kruskal(graph, 7)
