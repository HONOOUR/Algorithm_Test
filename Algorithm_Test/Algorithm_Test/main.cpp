//
//  main.cpp
//  Algorithm_Test
//
//  Created by jieunChoi on 2020/11/28.
//  Copyright © 2020 jieunChoi. All rights reserved.
//

#include "Solution.cpp"
#include "Solution_Hash.cpp"
#include "Solution_DAG.cpp"
#include "Solution_Tree.cpp"
#include "Solution_Dijkstra.cpp"
#include "Solution_LongestSubstringWithoutRepeating.cpp"
#include "Solution_KSum.cpp"

#include <iostream>
#include <vector>

int main(int argc, const char * argv[]) {
    Solution_KSum ksum;
    ksum.fourSum(std::vector<int> {1,0,-1,0,-2,2}, 0);
    Solution_LongestSubstringWithoutRepeating longestSubstring;
//    longestSubstring.lengthOfLongestSubstring("pwwkew");
    longestSubstring.lengthOfLongestSubstring_2("pwwkew");
    
    Solution_Dijkstra *solution_dijkstra = new Solution_Dijkstra();
    auto graph_dijkstra = std::vector<std::vector<int>> {{1}, {0, 2, 4}, {1, 4, 3}, {2}, {1, 2}};
    solution_dijkstra->dijkstra_shortestPath(graph_dijkstra);
    
    Solution_Tree *solution_tree = new Solution_Tree();
    auto graph_short = std::vector<std::vector<int>> {{1,2,3}, {0}, {0}, {0}};
    solution_tree->shortestPathLength(graph_short);
    
    auto root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left = new TreeNode(15);
    root->right->right = new TreeNode(7);    
    solution_tree->levelOrder(root);
    
    // All Paths From Source to Target
    Solution_DAG *solution_dag = new Solution_DAG();
    auto graph = std::vector<std::vector<int>> {{1,2}, {3}, {3}, {}};
    solution_dag->allPathSourceTarget(graph);
    
    
    Solution_Hash *solution_hash = new Solution_Hash();
    auto tNode = new TreeNode(1);
    tNode->left = new TreeNode(2);
    tNode->right = new TreeNode(5);
    tNode->left->left = new TreeNode(3);
    tNode->left->left->left = new TreeNode(4);
    solution_hash->printTree(tNode);
    
    
    Solution *solution = new Solution();
    // Remove Duplicates from Sorted List
    auto list = new ListNode();
    list->val = 1;
    list->next = new ListNode();
    list->next->val = 2;
    list->next->next = new ListNode();
    list->next->next->val = 3;
    list->next->next->next = new ListNode();
    list->next->next->next->val = 3;
    list->next->next->next->next = new ListNode();
    list->next->next->next->next->val = 4;
    list->next->next->next->next->next = new ListNode();
    list->next->next->next->next->next->val = 4;
    list->next->next->next->next->next->next = new ListNode();
    list->next->next->next->next->next->next->val = 5;
    solution->deleteDuplicates(list);
    
    // Remove Duplicate Letters
    solution->removeDuplicateLetters("dtcbbkt");
    
    // Merge Sorted Array
    auto num1 = std::vector<int>{2, 6, 5};
    auto num2 = std::vector<int>{3, 1, 7};
    solution->mergeStart(num1, 3, num2, 3);
    
    auto lL1 = new ListNode();
    lL1->val = 2;
    lL1->next = new ListNode();
    lL1->next->val = 4;
    lL1->next->next = new ListNode();
    lL1->next->next->val = 3;

    // Add Two Numbers
    auto lL2 = new ListNode();
    lL2->val = 5;
    lL2->next = new ListNode();
    lL2->next->val = 6;
    lL2->next->next = new ListNode();
    lL2->next->next->val = 4;
    solution->addTwoNumbers(lL1, lL2);

    // Reverse Integer
    solution->reverse(5613);
    
    // Two Sum
    auto nums = std::vector<int>{1, 2, 3, 4, 5};
    int target = 9;
    solution->twoSum(nums, target);
    
    return 0;
}
