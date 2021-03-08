//
//  Solution_KSum.cpp
//  Algorithm_Test
//
//  Created by jieunChoi on 2021/03/08.
//  Copyright © 2021 jieunChoi. All rights reserved.
//

#include <stdio.h>
#include <algorithm>
#include <vector>

class Solution_KSum
{
public:
    std::vector<std::vector<int>> fourSum(std::vector<int> nums, int target)
    {
        std::sort(begin(nums), end(nums));
        return kSum(nums, target, 0, 4);
    }
    std::vector<std::vector<int>> kSum(std::vector<int> nums, int target, int start, int k)
    {
        std::vector<std::vector<int>> res;
        if (start == nums.size() || nums[start] * k > target || target > nums.back() * k)
        {
            return res;
        }
        else if (k == 2)
        {
            return twoSum_2(nums, target, start);
        }
        else
        {
            // start++
            // target-num[i]
            for (int i = start; i < nums.size(); ++i)
            {
                if (i == start || nums[i - 1] != nums[i])
                {
                    for (auto &set : kSum(nums, target - nums[i], i + 1, k - 1))
                    {
                        res.push_back({nums[i]});
                        res.back().insert(end(res.back()), begin(set), end(set));
                    }
                }
            }
            return res;
        }
    }

    std::vector<std::vector<int>> twoSum(std::vector<int> nums, int target, int start)
    {
        const int end = (int)nums.size();
        std::vector<std::vector<int>> res;
        std::vector<int> hashTable;
        for (int i=start; i<end; i++)
        {
            auto hash = nums[i]%target;
            hashTable[hash] = 1;
        }
        
        for (int i=start; i<end; i++)
        {
            auto hash = target-nums[i];
            if (hashTable[hash] == 1)
            {
                res.push_back({nums[i], hash});
            }
        }
        return res;
    }

    std::vector<std::vector<int>> twoSum_2(std::vector<int> nums, int target, int start)
    {
        const int end = (int)nums.size();
        std::vector<std::vector<int>> res;
        std::vector<int> tempNums;
        for (int i=start; i<end; i++)
        {
            if (res.empty() || res.back()[1] != nums[i])
            {
                if (std::count(tempNums.begin(), tempNums.end(), target-nums[i])!=0)
                {
                    res.push_back({target-nums[i], nums[i]});
                }
                tempNums.push_back(nums[i]);
            }
        }
        return res;
    }
};
