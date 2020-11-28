//
//  Solution.cpp
//  Algorithm_Test
//
//  Created by jieunChoi on 2020/11/28.
//  Copyright © 2020 jieunChoi. All rights reserved.
//
#include <cstdio>
#include <iostream>
#include <vector>
#include <stack>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    Solution() {}
    // Two Sum (https://leetcode.com/problems/two-sum/)
    std::vector<int> twoSum(std::vector<int>& nums, int target)
    {
        // iterate vector nums to check the same number. an create a new vector
        std::vector<int> newNums{};
        // nums[0] .... nums[x]
        // nums[1] .... nums[y]

        for (auto& num : nums)
        {
            // selet hash with hash function
            // 0 < hash < target-1
            auto hash = num % target;
            newNums[hash] += 1;
        }

        for (auto& i : nums)
        {
            auto hash = target - i;
            if (hash == i)
            {
                newNums[hash] = 2;
                return std::vector<int>{ hash, i };
            }
            else if (newNums[hash] == 1)
            {
                return std::vector<int>{ hash, i };
            }
        }
        return std::vector<int>{};
    }

    
    // Reverse Integer (https://leetcode.com/problems/reverse-integer/)
    int reverse(int x)
    {
        int n = 10;
        std::vector<int> newNum{}; // 3 1 6 5
        while (x != x % n) // x = 5613 561 56 5
        {
            // remainder of x divided b y n
            int remainder = x % n;
            newNum.push_back(remainder);
            // x = (x-remainer)
            x = (x - remainder) / 10;
        }

        int numReversed = 0;
        while (!newNum.empty())
        {
            // add end value and pop
            // 5 + 6 * 10 + 1 * 100 + 3 * 1000
            auto reverse = newNum.back();
            std::cout << "add number" << reverse << std::endl;

            numReversed += reverse;
            newNum.pop_back();
        }
        std::cout << "Reversed Number = " << numReversed << std::endl;
        return numReversed;
    }

    // Add Two Numbers (https://leetcode.com/problems/add-two-numbers/)
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2)
    {
        // linkedList lL1 , lL2
        // while (lL->next == nullptr)
        // #1
        // num1 = lL1 node * 10 + node->next * 10 + node->next->next * 10
        // num2 = lL2 node * 10 + node->next * 10 + node->next->next * 10

        // #2
        // create a new list
        // num = lL1 node + lL2 node
        // if (num > 10) -> num = num - 10 and add 1 to next node
        // num->next = lL1 node->next + lL2 node->next + 1 or not
        
        auto lL3 = new ListNode();
        int add = 0;
        auto l1Node = l1;
        auto l2Node = l2;
        auto *l3Node = lL3;

        while (l1Node != NULL)
        {
            l3Node->val = l1Node->val + l2Node->val + add;
            add = 0;
            if (l3Node->val >= 10)
            {
                l3Node->val = l3Node->val - 10;
                add = 1;
            }
            l1Node = l1Node->next;
            l2Node = l2Node->next;

            l3Node->next = new ListNode();
            l3Node = l3Node->next;
        }
        return lL3;
    }
    
    void mergeStart(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n) {

        // sum nums1 and nums2
        for (auto &num: nums2)
        {
            nums1.push_back(num);
        }
        // if (start index is smaller than end)
        // divide them by 2 and reculsively call mergesort
        // divide a array into to
        // and merge
        mergeSort(nums1, 0, m + n - 1);
    }

    void mergeSort(std::vector<int>& nums, int p, int r)
    {
        if (p < r)
        {
            int q = (p + r) / 2;
            mergeSort(nums, p, q);
            mergeSort(nums, q + 1, r);
            merge(nums, p, q, r);
        }
    }

    void merge(std::vector<int>& nums, int p, int q, int r)
    {
        int i = p, j = q + 1, k = p;
        std::vector<int> temp;
        temp.resize(r-p+1);

        // compare first index and middle one
        while (i <= q && j <= r)
        {
            if (nums[i] < nums[j])
            {
                temp[k++] = nums[i++];
            }
            else
            {
                temp[k++] = nums[j++];
            }
        }
        while (i <= q)
        {
            temp[k++] = nums[i++];
        }
        while (j <= r)
        {
            temp[k++] = nums[j++];
        }

        for (int z=p; z<=r; z++)
        {
            nums[z] = temp[z];
        }
    }
};
