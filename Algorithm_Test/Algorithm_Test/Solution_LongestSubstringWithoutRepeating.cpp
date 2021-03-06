//
//  Solution_LongestSubstringWithoutRepeating.cpp
//  Algorithm_Test
//
//  Created by jieunChoi on 2021/03/07.
//  Copyright © 2021 jieunChoi. All rights reserved.
//

#include <stdio.h>
#include <string>
#include <vector>

class Solution_LongestSubstringWithoutRepeating {
public:
    int lengthOfLongestSubstring(std::string s) {
        int count = 0;
        std::vector<bool> visited(200, false);
        for (auto value: s)
        {
            int hashKey = value;
            if (!visited[hashKey
                         ])
            {
                ++count;
                visited[value] = true;
            }
        }
        
        return count;
    }
};
