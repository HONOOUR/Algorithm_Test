//
//  Solution_Tree.cpp
//  Algorithm_Test
//
//  Created by jieunChoi on 2020/12/13.
//  Copyright © 2020 jieunChoi. All rights reserved.
//
#include "TreeNode.h"
#include <stdio.h>
#include <vector>
#include <queue>
#include <cmath>

//Definition for a binary tree node.
//struct TreeNode {
//    int val;
//    TreeNode *left;
//    TreeNode *right;
//    TreeNode() : val(0), left(nullptr), right(nullptr) {}
//    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
//    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
//};

class Solution_Tree {
public:
    // Binary Tree Level Order Traversal (https://leetcode.com/problems/binary-tree-level-order-traversal/)
    std::vector<std::vector<int>> levelOrder(TreeNode* root) {
        std::queue<TreeNode*> queue;
        int h = height(root);
        int size = pow(2, h-1);
        std::vector<std::vector<int>> result(size);
        int index = 0;
        queue.push(root);
        result[index].push_back(root->val);
      
        while (!queue.empty()) {
            auto tempNode = queue.front();
            if ((tempNode->left != nullptr) || (tempNode->right != nullptr))
            {
                ++index;
                if (tempNode->left != nullptr)
                {
                    queue.push(tempNode->left);
                    result[index].push_back(tempNode->left->val);
                }
                if (tempNode->right != nullptr)
                {
                    queue.push(tempNode->right);
                    result[index].push_back(tempNode->right->val);
                }
                queue.pop();
            }
        }
        return result;
    }
    
    int height(TreeNode* root)
    {
        // return the max value between left and right height
        if (root == nullptr)
        {
            return 0;
        }
        else
        {
            int leftHeight = height(root->left);
            int rightHeight = height(root->right);
            int height;
            
            if (leftHeight > rightHeight)
            {
                height = leftHeight;
            }
            height = rightHeight;
            return height + 1;
        }
    }
    
    // Shortest Path Visiting All Nodes (https://leetcode.com/problems/shortest-path-visiting-all-nodes/)
    int shortestPathLength_(std::vector<std::vector<int>>& graph)
    {
        std::vector<std::vector<int>> path;
        for (int startNode = 0; startNode <= graph.size(); startNode++)
        {
            int distance = 0;
            std::vector<int> visited (graph.size(), 0);
            std::queue<std::pair<std::vector<int>, int>> queue;
            queue.push(std::pair<std::vector<int>, int> ({startNode}, startNode)); // (visited node, current node)
            while (!queue.empty()) {
                auto front = queue.front().first.back();
//                for (auto v: graph[front])
//                {
//
//                    auto cover = queue.front().first;
//                    cover.push_back(v);
//                    queue.push(std::pair<std::vector<int>, int> (cover, v));
//                    path.push_back(queue.front().first);
//                }
//                queue.pop();
            }
        }

        return 0;
    }
    int shortestPathLength(std::vector<std::vector<int>>& graph)
    {
        int distance=0;
        
        for (int startNode = 0; startNode <= graph.size(); startNode++)
        {
            std::vector<bool> visited (graph.size(), false);
            std::queue<int> queue;
            queue.push(startNode);
            
            while (!queue.empty())
            {
                for (auto v: graph[queue.front()])
                {
                    // not visited node?
                    if (!visited[v])
                    {
                        distance++;
                        queue.push(v);
                    }
                    else if (graph[queue.front()].size() == 1)
                    {
                        distance++;
                        queue.push(v);
                    }
                }
                visited[queue.front()] = true;
                queue.pop();
            }
        }
        return distance;
    }
};
