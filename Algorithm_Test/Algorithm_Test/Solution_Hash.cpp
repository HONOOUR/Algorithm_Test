//
//  Solution_Hash.cpp
//  Algorithm_Test
//
//  Created by jieunChoi on 2020/11/29.
//  Copyright © 2020 jieunChoi. All rights reserved.
//

#include <stdio.h>
#include <vector>
#include <string>
#include <iostream>
#include <queue>

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution_Hash {
public:
    std::vector<std::vector<std::string>> printTree(TreeNode* root)
    {
        // row  == height of bt
        // column == odd num
        // first node sholud be in the middle
        // left right traversal -> height++
        bFSearch(root);
        
        return std::vector<std::vector<std::string>> ();
    }
    
    void bFSearch(TreeNode* root)
    {
        std::vector<TreeNode*> arrayVisited;
        std::queue<TreeNode*> bfsQueue;
        arrayVisited.push_back(root);
        bfsQueue.push(root);
        while (!bfsQueue.empty())
        {
            walkTree(root, arrayVisited, bfsQueue);
        }
    }
    
    void walkTree(TreeNode* node, std::vector<TreeNode*>& arrayVisited, std::queue<TreeNode*>& bfsQueue)
    {
        if (node != nullptr)
        {
            
            walkTree(node->left, arrayVisited, bfsQueue);
            walkTree(node->right, arrayVisited, bfsQueue);
            
            for (auto i: arrayVisited)
            {
                if (i == node)
                {
                    continue;
                }
            }
            
            arrayVisited.push_back(node);
            std::cout << "add to arrayVisited node: " << node->val << std::endl;
            bfsQueue.push(node);
            std::cout << "enqueue to bfsQueue node: " << node->val << std::endl;
        }
        bfsQueue.pop();
    }
};
