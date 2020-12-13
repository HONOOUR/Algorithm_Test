//
//  Solution_DAG.cpp
//  Algorithm_Test
//
//  Created by jieunChoi on 2020/12/12.
//  Copyright © 2020 jieunChoi. All rights reserved.
//

#include <vector>
#include <queue>
#include <iostream>

class Solution_DAG {
public:
    // All Paths From Source to Target (https://leetcode.com/problems/all-paths-from-source-to-target/)
    std::vector<std::vector<int>> allPathSourceTarget(std::vector<std::vector<int>>& graph)
    {
        // graph[0] = [1, 2]
        // graph[1] = [3]
        // graph[2] = [3]
        
        // BFS
        int start = 0;
        int finish = (int)graph.size()-1;
        auto resultPath = BFS(graph, start, finish);
        
        // DFS recursive function to print all paths from start to finish node
        // path[] stores actual vertices
        // path_index is current index in path[]
        
        // visited
        std::vector<bool> visited (graph.size(), false);
        // path
        std::vector<int> path (graph.size());
        // all path
        std::vector<std::vector<int>> allPath (graph.size());

        for (int v = 0; v < visited.size(); v++)
        {
            DFS_TopologicalSort(graph, visited, path, v, v, finish);
        }
        
        // find all possible paths from node 0 to node n-1
        return std::vector<std::vector<int>>();
    }
    
    std::vector<int> DFS_TopologicalSort(std::vector<std::vector<int>>& graph, std::vector<bool> visited, std::vector<int> path, int vertex, int path_index, int finish)
    {
        std::vector<int> tempPath (finish);
        visited[vertex] = true;
        path[path_index] = vertex;
        path_index++;
        
        if (vertex == finish)
        {
            tempPath.resize(path_index);
            for (int i = 0; i < path_index; i++)
             {
                 std::cout << path[i] << " ";
                 tempPath[i] = path[i];
             }
            std::cout << std::endl;
        }
        else
        {
            //Recur for all the vertices adjacent to current vertex
            for (auto v: graph[vertex])
            {
                if (!visited[v])
                {
                    DFS_TopologicalSort(graph, visited, path, v, path_index, finish);
                }
            }
        }
        // Remove current vertex from path[] and mark it as unvisited
        path_index--;
        visited[vertex] = false;
        
        return tempPath;
    }
    
    // BFS
    std::vector<std::vector<int>> BFS (std::vector<std::vector<int>>& graph, int startVertex, int finishVertex)
    {
        std::vector<std::vector<int>> resultPath(finishVertex+1);
        
        // create a queue to insert a list of vertice to find neighbours
        std::queue<std::vector<int>> tempQueue;
        
        // push a start node
        tempQueue.push({startVertex}); // {0}
        while (!tempQueue.empty())
        {
            auto verticesPath = tempQueue.front(); // {0} {0, 1} {0, 2} {0, 1, 3} {0, 2, 1} {0, 2, 3} {0, 2, 1, 3}
            auto vertex = verticesPath.back(); // 0 1 2 3 1 3 3
            for (auto v: graph[vertex])
            {
                auto tempPath = verticesPath;
                tempPath.push_back(v);
                // enqueue a list of path from 0 to n
                tempQueue.push(tempPath);
                if (v == finishVertex)
                {
                    resultPath.push_back(tempPath);
                }
            }
            tempQueue.pop();
        }
        return resultPath;
    }
};
