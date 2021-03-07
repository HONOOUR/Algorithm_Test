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

class Solution_LongestSubstringWithoutRepeating
{
public:
    int lengthOfLongestSubstring(std::string s)
    {
        int maxCount = 0;
        int hashKey = 0;
        std::vector<int> substringNode(50, 0);
        std::vector<std::vector<int>> hashTable(s.size(), {0}); // hashTable[97] = {3, 3, 4}
        
        // read from first to end
        for (auto value: s)
        {
            // init
            if (hashKey == 0)
            {
                ++hashKey;
                // init hash value
                // create node for substring
                substringNode = {value};
                hashTable[hashKey] = std::vector<int> {1};
                maxCount = 1;
            }
            else // if there is hashkey, check if the value is in hashvalue
            {
                ++hashKey;
                bool isSubstring = false;
                for (auto item: substringNode)
                {
                    if (item == value)
                    {
                        isSubstring = true;
                    }
                }
                
                if (isSubstring) // create a new hash table
                {
                    // add substring node count to hashTable
                    int count = (int)substringNode.size();
                    maxCount = count > maxCount ? count : maxCount;
                    hashTable[hashKey].push_back(count);
                    //the value becomes hashkey
                    //init substring node
                    substringNode = {value};
                }
                else
                {
                    substringNode.push_back(value);
                }
            }
        }
        
        return maxCount;
    }
    
    int lengthOfLongestSubstring_2(std::string s)
    {
        std::string substring;
        int maxCount = 0;
        for (int i=0; i<s.size(); i++)
        {
            substring.push_back(s[i]);
            for (int j=i+1; j<s.size(); j++)
            {
                int count = 0;
                // check
                if (isUnique(i, j, s))
                {
                    substring.push_back(s[j]);
                }
                else
                {
                    count = (int)substring.size();
                    maxCount = maxCount > count ? maxCount : count;
                    substring = std::string();
                    break;
                }
            }
        }
        
        return maxCount;
    }
    
    bool isUnique(int start, int end, std::string s)
    {
        for (int i=start; i<end; i++)
        {
            if (s[i] == s[end])
            {
                return false;
            }
        }
        
        return true;
    }
};
