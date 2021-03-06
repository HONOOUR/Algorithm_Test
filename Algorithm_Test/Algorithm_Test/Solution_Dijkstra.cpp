//
//  Solution_Dijkstra.cpp
//  Algorithm_Test
//
//  Created by jieunChoi on 2020/12/27.
//  Copyright © 2020 jieunChoi. All rights reserved.
//

#include <stdio.h>
#include <queue>
#include <set>
#include <vector>

#define INF 1000000

class Solution_Dijkstra {
public:
    void dijkstra_shortestPath(std::vector<std::vector<int>>& graph) {
        // vector for distances
        // set all elem in distance to INF
        std::vector<int> distances(graph.size(), INF);
        // queue for vertices and their weight
        std::queue<int> vertexToWeight;
        // vertor for visited
        std::vector<bool> visited(graph.size(), false);
        
        std::pair<int, std::queue<int>> currentToPath;
        
        // set the elem of start node to 0
        int startVertex = 0;
        int weight = 1;
        vertexToWeight.push(startVertex);
        distances[startVertex] = 0;
        visited[startVertex] = true;
        currentToPath.first = startVertex;
        
        while (!vertexToWeight.empty()) {
            // check the front from the queue
            // enqueue adjacent vertices
            auto vertex = vertexToWeight.front();
            for(auto v: graph[vertex])
            {
                // not start node
                if (v == startVertex || visited[v])
                {
                    continue;
                }
                // compare the weight
                if (distances[v] > weight + distances[vertex])
                {
                    distances[v] = weight + distances[vertex];
                    if (vertex == currentToPath.first)
                    {
                        currentToPath.first = v;
                        currentToPath.second.push(v);
                    }
                    vertexToWeight.push(v);
                }
            }

            if (!visited[vertex])
            {
                visited[vertex] = true;
            }
            vertexToWeight.pop();
        }
    }
};
