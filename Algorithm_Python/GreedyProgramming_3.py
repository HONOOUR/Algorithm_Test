import sys
from typing import no_type_check_decorator

# https://leetcode.com/problems/jump-game-ii/


def getJumpToLast(nums):
    jump_count = 0
    left = right = 0  # start point
    while right < len(nums):
        farthest = 0
        for i in range(left, right+1):
            farthest = max(farthest, i + nums[i])
        left = right + 1
        right = farthest
        jump_count += 1

    return jump_count


nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]
getJumpToLast(nums)

# https://leetcode.com/problems/jump-game/


def canJumpNums(nums):
    answer = True
    if len(nums) == 1 and nums[0] == 0:
        return answer

    jump_count = 1
    for i in range(len(nums)-2, -1, -1):
        # 이전에 나오는 수가 다음 수로 점프할수 있는것이 가능한지 (횟수는 중요하지 않음)
        if nums[i] >= jump_count:
            jump_count = 1
            answer = True
            continue
        else:
            jump_count += 1
            answer = False
    return answer


nums = [2, 0]
canJumpNums(nums)
