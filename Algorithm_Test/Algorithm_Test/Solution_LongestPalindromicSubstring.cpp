//
//  Solution_LongestPalindromicSubstring.cpp
//  Algorithm_Test
//
//  Created by jieunChoi on 2021/03/13.
//  Copyright © 2021 jieunChoi. All rights reserved.
//

#include <string>
#include <vector>

class Solution_LongestPalindromicSubstring {
public:
    std::vector<char> longestPalindrome(std::string s) {
        
        std::vector<std::vector<char>> substring(s.size());
        for(int i=0; i<s.size(); i++)
        {
            for(int j=i; j<s.size(); j++)
            {
                substring[i].push_back(s[j]);
                
            }
        }

        // check the substring is palindrome
         // could be result
        std::vector<char> longestSubstring;
        for (int i=0; i<s.size(); i++)
        {
            std::vector<char> res;
            for(auto character : substring[i])
            {
                res.push_back(character);
                if (res.size()==1 && longestSubstring.size()==0)
                {
                    longestSubstring={res.front()};
                }
                else if (res.front() == res.back())
                {
                    bool isPalindrom = true;
                    std::vector<char> temp;
                    for(int j=0; j<res.size()/2; j++)
                    {
                        if(res[j] != res[res.size()-1-j])
                        {
                            isPalindrom = false;
                        }
                    }
                    if(isPalindrom && longestSubstring.size()<res.size())
                    {
                        longestSubstring = res;
                    }
                        
                }
            }
        }
        return longestSubstring;
    }
};
