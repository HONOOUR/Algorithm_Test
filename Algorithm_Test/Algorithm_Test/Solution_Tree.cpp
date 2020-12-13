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
        std::vector<std::vector<int>> result(h);
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
            
            if (leftHeight > rightHeight)
            {
                return leftHeight + 1;
            }
            return rightHeight + 1;
        }
    }
};
