//
//  main.cpp
//  Algorithm_Test
//
//  Created by jieunChoi on 2020/11/28.
//  Copyright © 2020 jieunChoi. All rights reserved.
//

#include "Solution.cpp"
#include <iostream>
#include <vector>

int main(int argc, const char * argv[]) {
    Solution *solution = new Solution();
    auto num1 = std::vector<int>{2, 6, 5};
    auto num2 = std::vector<int>{3, 1, 7};
    solution->mergeStart(num1, 3, num2, 3);
    
    auto lL1 = new ListNode();
    lL1->val = 2;
    lL1->next = new ListNode();
    lL1->next->val = 4;
    lL1->next->next = new ListNode();
    lL1->next->next->val = 3;

    auto lL2 = new ListNode();
    lL2->val = 5;
    lL2->next = new ListNode();
    lL2->next->val = 6;
    lL2->next->next = new ListNode();
    lL2->next->next->val = 4;

    solution->addTwoNumbers(lL1, lL2);

    // Reverse Integer
    solution->reverse(5613);
    
    //Two Sum
    auto nums = std::vector<int>{1, 2, 3, 4, 5};
    int target = 9;
    solution->twoSum(nums, target);
    
    return 0;
}
