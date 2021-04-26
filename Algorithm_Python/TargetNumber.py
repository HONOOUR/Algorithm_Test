from collections import deque


class TargetNumber:
    def getTargetAnswers(self, nums: list, target: int):
        answer = 0
        queue = deque([(0, 0)])
        while queue:
            s, l = queue.popleft()  # sum, level
            queue.append((s+nums[l-1], l+1))
            queue.append((s-nums[l-1], l+1))

            # sum==target && level==len(nums)
            if s == target and l == len(nums):
                answer += 1

        return answer


instance = TargetNumber()
print(instance.getTargetAnswers([1, 1, 1, 1, 1], 3))
